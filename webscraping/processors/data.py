from anytree import NodeMixin


class FileNode(NodeMixin):
    """
        Estrutura utilizada para representar um Diretório ou Arquivo na árvore de estruturas de arquivos do repositório.

        FileNode atua como um Node da lib anytree.
    """

    def __init__(self, name, lines=None, size_bytes=None, parent=None, children=None):
        self.name = name
        self.lines = lines
        self.size_bytes = size_bytes
        self.parent = parent
        if children:
            self.children = children

    def __str__(self):
        if self.lines:
            return "%s (%s linhas)" % (self.name, self.lines)
        return self.name

    def is_countable_file(self):
        return self.lines is not None and self.size_bytes is not None
