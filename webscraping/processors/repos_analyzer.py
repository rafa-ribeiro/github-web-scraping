from anytree import PreOrderIter


class Statistic:

    def __init__(self, extension, total_lines=0, total_bytes=0):
        self.extension = extension
        self.total_lines = total_lines
        self.total_bytes = total_bytes


def analyze_repo(root):
    total_lines_repo = 0
    extensions_dict = {}

    total_bytes_files = 0

    others_extension = "Outros"

    for node in PreOrderIter(root):
        if node.is_leaf:
            split_name = node.name.split(".")
            size_split_name = len(split_name)

            if node.lines and node.size_bytes:
                total_lines_repo = total_lines_repo + node.lines
                total_bytes_files = total_bytes_files + node.size_bytes

                if size_split_name > 1:
                    extension = split_name[size_split_name - 1]

                    if not extensions_dict.__contains__(extension):
                        extensions_dict[extension] = Statistic(extension)

                    statistic = extensions_dict[extension]

                    # TODO: converter no momento de jogar a informação em MyNode
                    statistic.total_lines = statistic.total_lines + node.lines
                    statistic.total_bytes = statistic.total_bytes + node.size_bytes

                    extensions_dict[extension] = statistic
                else:
                    if not extensions_dict.__contains__(others_extension):
                        extensions_dict[others_extension] = Statistic(others_extension)

                    statistic = extensions_dict[others_extension]

                    statistic.total_lines = statistic.total_lines + node.lines
                    statistic.total_bytes = statistic.total_bytes + node.size_bytes

                    extensions_dict[others_extension] = statistic

    print("Qtde de linhas Total do repositório: %s" % total_lines_repo)
    print("Qtde de bytes Total do repositório %s" % total_bytes_files)
    print("Extension    |   Lines   |   Bytes")
    for key, statistic in extensions_dict.items():
        print("%s   |   %s  |   %s" % (key, statistic.total_lines, statistic.total_bytes))
