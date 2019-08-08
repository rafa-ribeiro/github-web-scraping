def open_file(file_path):
    try:
        file = open(file_path, "r")
        if file.mode == 'r':
            return file.read()
    except Exception as e:
        raise Exception("Erro ao ler o arquivo %s\nMessage:\n%s" % (file_path, e))


def get_repositories_list(file_path):
    """
    Retorna uma lista de string contendo cada linha do arquivo lido.

    :param file_path: Path do arquivo a ser lido.
    :return: Lista de str contendo as linhas lidas.
    """
    try:
        with open(file_path, "r") as file:
            return file.readlines()
    except Exception as e:
        raise Exception("Erro ao ler o arquivo %s\nMessage:\n%s" % (file_path, e))


def write_file(file_path, content):
    """
    Escreve o conteúdo informado em disco.

    :param file_path: Contendo diretório + nome do arquivo em que o arquivo gerado será colocado,
    :param content: Conteúdo do arquivo a ser escrito.
    """
    try:
        with open(file_path, "a+") as file:
            file.write(content)
        print("Arquivo gerado com sucesso em {}".format(file_path))
    except Exception as e:
        raise Exception("Erro ao escrever o arquivo %s\nMessage:\n%s" % (file_path, e))

