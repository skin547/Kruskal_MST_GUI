from tkinter import Tk, Canvas, Button, simpledialog, messagebox
from node import node
from edge import edge
from tree import tree

root = Tk()
root.title("cycle_detect")
canvas = Canvas(root, width=800, height=600, bg="#A7A8AA")

global nid, eid
nid = 0
eid = 0
node_set = []  # stores all nodes
tree_set = []  # stores all trees


def draw_circle(event):
    global nid, node_set
    new_node = node(nid, event.x, event.y, 30)
    new_node.draw(canvas)
    nid += 1
    node_set.append(new_node)


def draw_line():
    global node_set, eid
    A = simpledialog.askinteger("Input Node A", "Input Node A ID")
    B = simpledialog.askinteger("Input Node B", "Input Node B ID")
    weight = simpledialog.askinteger("Weight", "Input Weight")
    nodeA = search_node(A, node_set)
    nodeB = search_node(B, node_set)
    if (nodeA and nodeB):
        new_edge = edge(eid, nodeA, nodeB, weight)
        eid += 1
        new_edge.draw(canvas)
        if(cycle_detect(nodeA, nodeB)):
            messagebox.showinfo("Cycle", "Oops, a Cycle")
        nodeA.connect(nodeB)
        append_tree(nodeA.getTree())
        nodeA.getTree().add_edge(new_edge)


def append_tree(tree):
    if(tree not in tree_set):
        tree_set.append(tree)


def search_node(tid, subset):
    for tnode in subset:
        if (tnode.getId() == tid):
            return tnode
    messagebox.showwarning("Invalid ID", "please Input a valid ID")
    return None


def cycle_detect(nodeA, nodeB):  # if two nodes are in the same tree then there will be a cycle
    if (nodeA.getTree() == nodeB.getTree()):
        return True
    return False


def FindMST():  # Find MST of biggest tree
    max = 0
    for tree in tree_set:
        if(max < len(tree.getNodes())):
            max = len(tree.getNodes())
            max_tree = tree
    Kruskal(max_tree)


def Kruskal(t):
    MST = tree(t.getId())
    nodes = t.getNodes()
    edges = sorted(t.getEdges())
    size = len(nodes)-1
    for node in nodes:  # Set each node as a MST
        newTree = tree(node.getId())
        node.setTree(newTree)
        newTree.add(node)  # Root
    while size > 0:
        edge = edges.pop(0)
        nodeA = edge.getNodeA()
        nodeB = edge.getNodeB()
        if(cycle_detect(nodeA, nodeB)):  # If have cycle then reject
            continue
        MST.add_edge(edge)
        nodeA.getTree().connectList(nodeB)  # Connect two MST
        size -= 1
    change_color(MST.getEdges())


def change_color(collection):  # Change widget's attribute
    for item in collection:
        i = item.getShape()
        canvas.itemconfig(i, fill="red")

canvas.bind('<Button-1>', draw_circle)
canvas.pack(side="top")

Draw_Button = Button((root), text='Draw Line', width=30, height=2, command=draw_line)
Draw_Button.pack()

MST_Button = Button((root), text='Find MST', width=30, height=2, command=FindMST)
MST_Button.pack()

root.mainloop()
