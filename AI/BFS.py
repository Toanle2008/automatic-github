from collections import defaultdict

data = defaultdict(list)
data["A"] = ["B", "C", "D"]
data["B"] = ["E", "F"]
data["C"] = ["G", "H"]
data["D"] = ["I", "J"]
data["F"] = ["K", "L", "M"]
data["H"] = ["N", "O"]
data["I"] = ["P"]

class node:
    
    def __init__(self, value, head=None):
        self.value = value
        self.head = head


def BFS(begin, end):
    open = []
    close = []
    open.append(begin)
    while True:
        if len(open) == 0:
            print("fail!")
            return
        curr = open.pop(0)
        close.append(curr)
        
        if curr.value == end.value:
            print("success!")
            while curr.head != None:
                print(curr.value)
                curr = curr.head
            return

        for obj in data[curr.value]:
            tmpNode = node(obj)
            tmpNode.head = curr
            if tmpNode not in open and tmpNode not in close:
                open.append(tmpNode)

BFS(node("E"), node("J"))