from util import *


_LOWER_CASE = " ^^^^^abcdefghijklmnopqrstuvwxyz"
_UPPER_CASE = " ^^^^^ABCDEFGHIJKLMNOPQRSTUVWXYZ"
_PUNCTUATION = " ^^^^^^\n0123456789.,!?_#’\"/\\-:()"
_CHARACTER_MAP = {0: _LOWER_CASE,  1: _UPPER_CASE, 2: _PUNCTUATION}

_FIRST_CHAR = 0x7C00
_SECOND_CHAR = 0x03E0
_THIRD_CHAR = 0x001F
_END_MARKER = 0x8000


def get_characters(word):
    characters = []
    characters.append((word & _FIRST_CHAR) >> 10)
    characters.append((word & _SECOND_CHAR) >> 5)
    characters.append((word & _THIRD_CHAR))
    if (word & _END_MARKER) == _END_MARKER:
        characters.append(_END_MARKER)
    return characters


def decode_characters(characters, abbreviation_table=None):
    alphabet = 0
    offset = 0
    abbreviation = False
    s = ""

    if len(characters) >= 5 and characters[0] == 5 and characters[1] == 6:
        # 10bit ZSCII code
        s += chr(((characters[2] & 0x1f) << 5) + (characters[3] & 0x1f))
        return s + decode_characters(characters[4:], abbreviation_table)

    for c in characters:
        if abbreviation_table is not None and abbreviation and alphabet == 2:
            s += abbreviation_table[offset+c].text
            offset=0
            alphabet=0
            abbreviation=False
        else:
            if c == 0:
                s += " "
                alphabet=0
            elif c < 4:
                alphabet=2
                offset=(c - 1) * 32
                abbreviation=True
            elif c <= 5:
                alphabet=c - 3
            elif c == _END_MARKER:
                pass
            else:
                s += _CHARACTER_MAP[alphabet][c]
                alphabet=0
    return s
