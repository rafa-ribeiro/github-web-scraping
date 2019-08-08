from anytree import PreOrderIter


class RepoMetrics:

    def __init__(self, total_lines_repo, total_bytes_repo, statistics):
        self.total_lines_repo = total_lines_repo
        self.total_bytes_repo = total_bytes_repo
        self.statistics = statistics

    def calculate_percent_lines(self, statistic):
        return statistic.total_lines * 100 / self.total_lines_repo if self.total_lines_repo != 0 else 0

    def calculate_percent_bytes(self, statistic):
        return statistic.total_bytes * 100 / self.total_bytes_repo if self.total_bytes_repo != 0 else 0


class Statistic:

    def __init__(self, extension, total_lines=0, total_bytes=0):
        self.extension = extension
        self.total_lines = total_lines
        self.total_bytes = total_bytes


def analyze_repo(root):
    extensions_dict = {}
    total_lines_repo = 0
    total_bytes_repo = 0
    others_extension = "Outros"

    for node in PreOrderIter(root):
        if node.is_leaf:
            if node.is_countable_file:
                total_lines_repo = total_lines_repo + node.lines
                total_bytes_repo = total_bytes_repo + node.size_bytes

                split_name = node.name.split(".")
                size_split_name = len(split_name)

                if size_split_name > 1:
                    extension = str(split_name[size_split_name - 1]).lower()

                    if not extensions_dict.__contains__(extension):
                        extensions_dict[extension] = Statistic(extension)

                    statistic = extensions_dict[extension]
                    statistic.total_lines = statistic.total_lines + node.lines
                    statistic.total_bytes = statistic.total_bytes + node.size_bytes
                else:
                    if not extensions_dict.__contains__(others_extension):
                        extensions_dict[others_extension] = Statistic(others_extension)

                    others_statistic = extensions_dict[others_extension]
                    others_statistic.total_lines = others_statistic.total_lines + node.lines
                    others_statistic.total_bytes = others_statistic.total_bytes + node.size_bytes

    return RepoMetrics(total_lines_repo, total_bytes_repo, extensions_dict.values())
