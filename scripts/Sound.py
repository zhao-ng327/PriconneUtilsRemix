import os
import re
import shutil
import multiprocessing
from concurrent.futures import ThreadPoolExecutor

import requests

import Constants

def generate_list(snd_name: str, snd_dir: str) -> tuple[list[str], list[str]]:
    if not os.path.isdir(snd_dir):
        os.makedirs(snd_dir)

    name = []
    hash = []

    with open(Constants.SOUNDMANIFEST, 'r') as f:
        for lines in f:
            l = lines.split(',')
            n = l[0].split('/')[-1]
            h = l[2]

            if re.fullmatch(snd_name, n):
                name.append(os.path.join(snd_dir, n))
                hash.append(h)
    
    return name, hash


def download_file(name: str, hash: str):
    dirName = os.path.dirname(name)
    realFileName = os.path.basename(name).split(".")[0]

    hadDL = check_file(re.compile(f'{realFileName}.*\.(acb|awb)'), dirName)

    if not os.path.isfile(name) and hadDL is False:
        print(f'Downloading {name}...')
        r = requests.get(f'{Constants.SOUND_URL}/{hash[:2]}/{hash}').content
        with open(name, 'wb') as f:
            f.write(r)

    else:
        print(f'File [{name}] already exists')

'''
def convert_WAV(args):
    name, mode = args
    realFilename = os.path.basename(name).split(".")[0]

    if os.path.exists(name) and name.endswith('.awb'):
        wav_dir = getattr(Constants, f"{mode}_WAV_DIR")
        if not os.path.exists():
            os.makedirs(wav_dir)
        wav_path = os.path.join(wav_dir, f"{realFilename}_?s.wav")
        with open(os.devnull, 'w') as devnull:
            os.system(f'cd {Constants.VGMSTREAM_DIR} && vgmstream-cli.exe -S 0 -o {wav_path} {name} > {os.devnull} 2>&1')
'''

def convert_MP3(args):
    name, mode = args
    realFilename = os.path.basename(name).split(".")[0]

    if os.path.exists(name) and name.endswith('.awb'):
        mp3_dir = getattr(Constants, f"{mode}_MP3_DIR")
        if not os.path.exists(mp3_dir):
            os.makedirs(mp3_dir)
        mp3_path = os.path.join(mp3_dir, f"{realFilename}_?s.mp3")
        with open(os.devnull, 'w') as devnull:
            os.system(f'cd {Constants.VGMSTREAM_DIR} && vgmstream-cli.exe -S 0 -o {mp3_path} {name} > {os.devnull} 2>&1')



def check_file(fn: str, fd: str) -> bool:
    for file in os.listdir(fd):
        a: re.Match = re.search(fn, file)
        if a: 
            return True
    
    return False


def sound() -> None:
    if not os.path.isfile(Constants.SOUNDMANIFEST):
        print("Please do DBCheck first before using this as the file needed to download stuff in this script is downloaded from DBCheck")
        input("Press ENTER to continue")
        return

    snd_type = input("Select sound type:\n1. voice\n2. bgm\n").strip()
    mode = "BGM"
    if snd_type == '1':
        mode = "VOICE"
        cmn_choice = input("Select voice type:\n1. cmn\n2. all\n").strip()
        if cmn_choice == '1':
            id_choice = input("Enter ID or 'all':\n").strip()
            if id_choice == 'all':
                snd_name = Constants.VOICE_NAME_CMN  # vo_cmn.+\.(acb|awb)
            else:
                snd_name = re.compile(f'vo_cmn_{id_choice}\.(acb|awb)')
        else:
            snd_name = Constants.VOICE_NAME
        snd_dir = Constants.VOICE_DIR
    else:
        snd_name = Constants.BGM_NAME
        snd_dir = Constants.BGM_DIR

    name, hash = generate_list(snd_name, snd_dir)

    with ThreadPoolExecutor() as thread:
        thread.map(download_file, name, hash)
    
    mode_list = [mode] * len(name)
    with multiprocessing.Pool() as pool:
        pool.map(convert_MP3, zip(name, mode_list))


    input(">> Download and conversion completed!\nPress ENTER to continue")


if __name__ == '__main__':
    sound()
