def open_file(file_path):
    try:
        file = open(file_path, "r")
        if file.mode == 'r':
            return file.read()
    except Exception as e:
        raise Exception("Erro ao ler o arquivo %s\nMessage:\n%s" % (file_path, e))


def get_repositories_list(file_path):
    try:
        with open(file_path, "r") as file:
            return file.readlines()
    except Exception as e:
        raise Exception("Erro ao ler o arquivo %s\nMessage:\n%s" % (file_path, e))


def write_file(file_path, content):
    try:
        with open(file_path, "a+") as file:
            file.write(content)
        print("Arquivo gerado com sucesso em {}".format(file_path))
    except Exception as e:
        raise Exception("Erro ao escrever o arquivo %s\nMessage:\n%s" % (file_path, e))

