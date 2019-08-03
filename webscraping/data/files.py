def open_file(filepath):
    try:
        file = open(filepath, "r")
        if file.mode == 'r':
            return file.read()
    except Exception as e:
        raise Exception("Erro ao ler o arquivo %s\nMessage:\n%s" % (filepath, e))
