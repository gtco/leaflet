from collections import namedtuple

from util import get_word
from text import get_characters, decode_characters, _END_MARKER

_WORD_COUNT = 96

Abbreviation = namedtuple("Abbreviation", ["characters", "text"])


def load_abbreviation(buffer, start, index):
    offset = start + (index * 2)
    packed_address = (get_word(buffer, offset) * 2)
    characters = []

    characters += get_characters(get_word(buffer, packed_address))
    while _END_MARKER not in characters:
        packed_address += 2
        characters += get_characters(get_word(buffer, packed_address))

    return characters


def load_table(buffer, start):
    table = {}
    for i in range(0, _WORD_COUNT):
        c = load_abbreviation(buffer, start, i)
        a = Abbreviation(c, decode_characters(c).strip())
        table[i] = a
    return table
