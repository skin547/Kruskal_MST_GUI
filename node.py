from tkinter import Tk, Canvas, Button, simpledialog, messagebox
from tree import tree


class node:
    def __init__(self, nid, x, y, r):
        self.__id = nid
        self.__x = x
        self.__y = y
        self.__r = r
        self.__tree = tree(nid)
        self.__tree.add(self)

    def draw(self, canvas):
        x = self.__x
        y = self.__y
        r = self.__r
        nid = self.__id
        self.__shape=canvas.create_oval(x - r, y - r, x + r, y + r, fill="white",tags="node")
        self.__text=canvas.create_text(x, y, text=str(nid))

    def connect(self, node):
        self.__tree.connectList(node)

    def getId(self):
        return self.__id

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setTree(self, tree):
        self.__tree = tree

    def getTree(self):
        return self.__tree
    def getShape(self):
        return self.__shape
    def clicked(self):
        print('clicked on a node')
        print(self.getX(),self.getY())
