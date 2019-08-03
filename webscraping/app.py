from webscraping.data.files import open_file


def main():
    repositories = open_file("/home/rafael/python-projects/vivadecora/webscraping/resources/repositories.txt")
    print("Conteúdo do arquivo:\n%s" % repositories)
    pass


if __name__ == '__main__':
    main()
