from collections import namedtuple

from util import get_byte, get_word
from text import get_characters


_separators = []
_entries = []

DictionaryEntry = namedtuple(
    "DictionaryEntry", ["position", "address", "characters"])


def load_entries(buffer, address):
    n = get_byte(buffer, address)

    for i in range(1, n+1):
        _separators.append(chr(get_byte(buffer, address + i)))

    length = get_byte(buffer, address + n + 1)
    count = get_word(buffer, address + n + 2)
    start = address + n + 4

    for j in range(0, count):
        characters = []
        a = (j*length) + start
        characters += (get_characters(get_word(buffer, a)))
        characters += (get_characters(get_word(buffer, a+2)))
        entry = DictionaryEntry(j, a, characters)
        _entries.append(entry)

    #print("# of separators {:02d}".format(n))
    #print("length {:02d}".format(length))
    #print("count {:02d}".format(count))
    #print("start {:04x}".format(start))
    return _entries
