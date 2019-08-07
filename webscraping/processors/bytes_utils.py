from enum import Enum


def get_multiplier(description):
    for unity in BytesUnity:
        if unity.description.__eq__(description):
            return unity.multiplier
    raise Exception("Erro! Unidade de medida não mapeada para conversão em Bytes: %s" % description)


class BytesUnity(Enum):
    BYTES = ("Bytes", 1)
    KB = ("KB", 1000)

    def __init__(self, description, multiplier):
        self.description = description
        self.multiplier = multiplier
