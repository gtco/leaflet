import sys

from util import *
from text import decode_characters
from dictionary import load_entries, DictionaryEntry
from abbreviation_table import load_table, Abbreviation
from object_table import load_objects


PAGED_MEMORY = 0x04
FIRST_INSTRUCTION = 0x06
DICTIONARY = 0x08
OBJECT_TABLE = 0x0A
GLOBAL_VARS = 0x0C
STATIC_MEM = 0x0E
ABBREVIATION_TABLE = 0x18


def main(argv):
    load_file(argv[0])


def load_file(filename):
    with open(filename, "rb") as f:
        buffer = f.read()
        if len(buffer) > 0x0F:
            print("paged memory {:04x}".format(get_word(buffer, PAGED_MEMORY)))
            print("first instruction {:04x}".format(
                get_word(buffer, FIRST_INSTRUCTION)))
            print("dictionary {:04x}".format(get_word(buffer, DICTIONARY)))
            print("object table {:04x}".format(get_word(buffer, OBJECT_TABLE)))
            print("global vars {:04x}".format(get_word(buffer, GLOBAL_VARS)))
            print("static memory {:04x}".format(get_word(buffer, STATIC_MEM)))
            table = load_table(buffer, get_word(buffer, ABBREVIATION_TABLE))
            entries = load_entries(buffer, get_word(buffer, DICTIONARY))
            objects = load_objects(buffer, get_word(buffer, OBJECT_TABLE))


if __name__ == "__main__":
    main(sys.argv[1:])
