
class tree:
    def __init__(self, tid):
        self.__nodes = []
        self.__edges = []
        self.__tid = tid

    def getNodes(self):
        return self.__nodes

    def add(self, node):
        self.__nodes.append(node)

    def add_edge(self,edge):
        self.__edges.append(edge)

    def connectList(self, node):
        nodes = node.getTree().getNodes()
        edges = node.getTree().getEdges()
        for node in nodes:
            if node in self.__nodes:
                continue
            self.add(node)
            node.setTree(self)
        for edge in edges:
            if edge in self.__edges:
                continue
            self.add_edge(edge)
            edge.setTree(self)

    def getId(self):
        return self.__tid

    def getEdges(self):
        return self.__edges
