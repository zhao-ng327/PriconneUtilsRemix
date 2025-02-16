from struct import Struct
from enum import Enum

UTFChunkHeader = Struct(">4sIIIIIHHI")
USMChunkHeader = Struct(">4sIBBHBBBBIIII")
CPKChunkHeader = Struct("<4sIII")
AWBChunkHeader = Struct("<4sBBHIHH")
SBTChunkHeader = Struct("<IIIII")
WavHeaderStruct = Struct("<4sI4s4sIHHIIHH") # This is wrong, FMT Struct should be on its own, away from RIFF.
WavSmplHeaderStruct = Struct("<4sIIIIIIIIIIIIIIII") # Supports only 1 looping point.
WavNoteHeaderStruct = Struct("<4sII")
WavDataHeaderStruct = Struct("<4sI")

class USMChunckHeaderType(Enum):
    CRID  = b"CRID" # Header.
    SFSH  = b"SFSH" # SofDec1 Header?
    SFV   = b"@SFV" # Video (VP9/H264/MPEG).
    SFA   = b"@SFA" # Audio (HCA/ADX).
    ALP   = b"@ALP" # Rare. (Alpha video information).
    CUE   = b"@CUE" # Rare. (Cue points).
    SBT   = b"@SBT" # Rare. (Subtitle information).
    AHX   = b"@AHX" # Rare. (Ahx audio file? Used for SofDec1 only?)
    USR   = b"@USR" # Rare. (User data?)
    PST   = b"@PST" # Rare. (Unknown).

class CPKChunkHeaderType(Enum):
    CPK   = b"CPK " # Header.
    TOC   = b"TOC " # Cpkmode 1, 2, 3.
    ITOC  = b"ITOC" # Cpkmode 0, 2.
    GTOC  = b"GTOC" # Cpkmode 3.
    ETOC  = b"ETOC" # Any CpkMode. Not important.
    HTOC  = b"HTOC" # Unknown.
    HGTOC = b"HGTOC"# Unknown.

class UTFType(Enum):
    UTF   = b"@UTF" # Header.
    EUTF  = b"\x1F\x9E\xF3\xF5" # Encrypted @UTF Header. Very likely exclusive to CPK's @UTF only.

class AWBType(Enum):
    AFS2  = b"AFS2" # Header.

class HCAType(Enum):
    HCA   = b"HCA\x00" # Header.
    EHCA  = b"\xC8\xC3\xC1\x00" # Encrypted HCA header.

class VideoType(Enum):
    IVF   = b"DKIF" # Header.
    # H264  = b"" # Header.
    # MPEG  = b"" # Header.

# I saw some devs swap the unsigned/signed indexes. So I am not sure what's correct or not.
# In my own experience, swapping those results in an incorrect signed values (should be unsigned) in ACB's/CPK's.
# If someone were to change this, they must change 'stringtypes' function in UTF/UTFBuilder classes.
class UTFTypeValues(Enum):
    uchar  = 0
    char   = 1
    ushort = 2
    short  = 3
    uint   = 4
    int    = 5
    ullong = 6
    llong  = 7
    float  = 8
    double = 9 # Does not seem to exist.
    string = 10
    bytes  = 11

class CriHcaQuality(Enum):
    Highest = 0
    High    = 1
    Middle  = 2
    Low     = 3
    Lowest  = 5