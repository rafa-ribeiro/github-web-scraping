from enum import Enum


def get_multiplier(description):
    """ Retorna um valor multiplicador utilizado para a conversão de unidades para Bytes em sistema decimal. """

    for unity in BytesUnity:
        if unity.description.__eq__(description):
            return unity.multiplier
    raise Exception("Erro! Unidade de medida não mapeada para conversão em Bytes: %s" % description)


class BytesUnity(Enum):
    """ Unidades de medida mapeadas passíveis de conversão para Bytes."""

    BYTES = ("Bytes", 1)
    KB = ("KB", 1000)

    def __init__(self, description, multiplier):
        self.description = description
        self.multiplier = multiplier
