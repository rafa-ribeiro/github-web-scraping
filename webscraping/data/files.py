def open_file(filepath):
    file = open(filepath, "r")
    if file.mode == 'r':
        return file.read()
