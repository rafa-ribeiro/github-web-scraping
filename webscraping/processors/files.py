def open_file(filepath):
    try:
        file = open(filepath, "r")
        if file.mode == 'r':
            return file.read()
    except Exception as e:
        raise Exception("Erro ao ler o arquivo %s\nMessage:\n%s" % (filepath, e))


def get_repositories(filepath):
    try:
        with open(filepath, "r") as file:
            return file.readlines()
    except Exception as e:
        raise Exception("Erro ao ler o arquivo %s\nMessage:\n%s" % (filepath, e))