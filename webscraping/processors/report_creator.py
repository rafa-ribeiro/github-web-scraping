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

    return "".join(output)


def break_line():
    return "{}".format("\n" * 2)
