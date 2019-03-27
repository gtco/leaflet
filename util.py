

def get_word(buffer, address):
    return (buffer[address] << 8) + buffer[address + 1]


def get_byte(buffer, address):
    return buffer[address]
