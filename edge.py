class edge:
    def __init__(self, eid, nodeA, nodeB,weight):
        self.__nodeA = nodeA
        self.__nodeB = nodeB
        self.__id = eid
        self.__x1 = nodeA.getX()
        self.__x2 = nodeB.getX()
        self.__y1 = nodeA.getY()
        self.__y2 = nodeB.getY()
        self.__weight = weight

    def __lt__(self, other):        #less than
         return self.getWeight() < other.getWeight()

    def draw(self, canvas):
        x1 = self.__x1
        x2 = self.__x2
        y1 = self.__y1
        y2 = self.__y2
        self.__shape=canvas.create_line(x1, y1, x2, y2) 
        self.__text=canvas.create_text((x1+x2)/2,(y1+y2)/2,text=str(self.__weight))
    
    def getWeight(self):
        return self.__weight
    
    def setWeight(self,weight):
        self.__weight = weight

    def getId(self):
        return self.__id

    def getShape(self):
        return self.__shape

    def getNodeA(self):
        return self.__nodeA

    def getNodeB(self):
        return self.__nodeB
    def setTree(self,Tree):
        self.__tree = Tree
