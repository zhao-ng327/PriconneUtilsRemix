import os
import re

CUR_DIR = os.getcwd()

# lib
CODE_DIR = os.path.join(CUR_DIR, 'scripts')
CONESHELL_DIR = os.path.join(CODE_DIR, 'Coneshell')
FFMPEG_DIR = os.path.join(CODE_DIR, 'ffmpeg')
VGMSTREAM_DIR = os.path.join(CODE_DIR, 'vgmstream-win64')

# DBCheck constants
CONFIG_FILE = os.path.join(CUR_DIR, 'config.json')
DB_DIR = os.path.join(CUR_DIR, 'database')
MAX_TEST = 20
TEST_MULTIPLIER = 10


# Movie constants
MOVIE_URL = 'http://prd-priconne-redive.akamaized.net/dl/pool/Movie'
MOVIE_DIR = os.path.join(CUR_DIR, 'movie')
MOVIEMANIFEST = os.path.join(DB_DIR, 'movie2manifest')

L2D_DIR = os.path.join(MOVIE_DIR, 'l2d')
L2D_NAME = re.compile('character_\d+_000002\.usm')

CUTIN_DIR = os.path.join(MOVIE_DIR, 'cutin')
CUTIN_NAME = re.compile('cutin_\d+\.usm')

SUMMON_DIR = os.path.join(MOVIE_DIR, 'summon')
SUMMON_NAME = re.compile('character_\d+_000001\.usm')

EVENT_DIR = os.path.join(MOVIE_DIR, 'event')
EVENT_NAME = re.compile('story_5\d{5}[7-9]0[1-2]\.usm')

MOVIE_TYPES = {
    'dir': {
        'cutin': CUTIN_DIR,
        'l2d': L2D_DIR,
        'summon': SUMMON_DIR,
        'event': EVENT_DIR
    },
    'name': {
        'cutin': CUTIN_NAME,
        'l2d': L2D_NAME,
        'summon': SUMMON_NAME,
        'event': EVENT_NAME
    }
}


# Sound constants
SOUND_URL = 'http://prd-priconne-redive.akamaized.net/dl/pool/Sound'
SOUND_DIR = os.path.join(CUR_DIR, 'sound')
SOUNDMANIFEST = os.path.join(DB_DIR, 'soundmanifest')

BGM_DIR = os.path.join(SOUND_DIR, 'bgm')
BGM_NAME = re.compile('bgm_.+\.(acb|awb)')

BGM_WAV_DIR = os.path.join(BGM_DIR, 'wav')
BGM_MP3_DIR = os.path.join(BGM_DIR, 'mp3')

VOICE_DIR = os.path.join(SOUND_DIR, 'voice')
VOICE_NAME = re.compile('vo_.+\.(acb|awb)')
VOICE_NAME_CMN = re.compile('vo_cmn.+\.(acb|awb)')

VOICE_WAV_DIR = os.path.join(VOICE_DIR, 'wav')
VOICE_MP3_DIR = os.path.join(VOICE_DIR, 'mp3')
