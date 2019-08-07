from anytree import NodeMixin, RenderTree


class MyNode(NodeMixin):

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
