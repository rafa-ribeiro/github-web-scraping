from webscraping.processors.repos_analyzer import RepoMetrics
from anytree import RenderTree


def create_report(repository, node_structure, repo_metrics):
    output = [
        "Repository: {}".format(repository),
        break_line(),
        "Estrutura de pastas do repositório",
        break_line()
    ]

    for pre, fill, node in RenderTree(node_structure):
        output.append("%s%s\n" % (pre, node.__str__()))

    output.append(break_line())
    output.append("Métricas por extensão de arquivos")
    output.append(break_line())
    output.append(get_border_table())
    output.append("|{:25}|{:25}|{:25}|\n".format("Extensão", "Linhas", "Bytes"))
    output.append(get_border_table())
    for statistic in repo_metrics.statistics:
        percent_lines = get_percent_lines_metrics(statistic.total_lines, repo_metrics.calculate_percent_lines(statistic))
        percent_bytes = get_percent_bytes_metrics(statistic.total_bytes, repo_metrics.calculate_percent_bytes(statistic))
        output.append("|{:25}|{:25}|{:25}|\n".format(statistic.extension, percent_lines, percent_bytes))

    output.append(get_border_table())
    return "".join(output)


def get_border_table():
    return "{}\n".format("-" * 79)


def get_percent_lines_metrics(total_value, percent):
    return "{:d} ({:4.2f} %)".format(total_value, percent)


def get_percent_bytes_metrics(total_value, percent):
    return "{:2f} ({:4.2f} %)".format(total_value, percent)


def break_line():
    return "{}".format("\n" * 2)
