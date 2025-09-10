import random

class edge:
    def __init__(self,p1,p2,w):
        self.p1 = p1
        self.p2 = p2
        self.w = w
    def __repr__(self):
        return(f"{self.p1}{self.p2}")


def func(list):
    global current
    Aalert = []
    Balert = []

    current.append(list[0])
    a = current[-1].p1
    b = current[-1].p2

    for i in current:
        if (i.p1 == a) or (i.p2 == a):
            Aalert.append(i)
        elif (i.p1 == b) or (i.p2 == b):
            Balert.append(i)
    if (len(Aalert) != 0) and (len(Balert) != 0):
        current.pop()
        return False
    
    return True

        





def prim(e , v):
    global current
    current = []
    start = v[0]
    sorted = []
    flag = True
    cnt = 0
    while flag:
        sorted.clear()
        for i in e:
            if i.p1 == start or i.p2 == start:
                sorted.append(i)
        sorted.sort(key = lambda edge: edge.w)
        if func(sorted):
            start = sorted[0].p1 if sorted[0].p1 != start else sorted[0].p2
        else:
            sorted.pop(0)
            start = sorted[0].p1 if sorted[0].p1 != start else sorted[0].p2
        cnt += 1
        if cnt == len(v)-1:
            flag = False

    print(current)


        
        



def runprim():
    alpha = "abcdefghijklmnopqrstuvwxyz"
    size = int(input("How many vertices?(max 26): "))
    vertices = []
    edges = []
    for i in range(size):
        vertices.append(alpha[i])
    flag = True
    while flag:
        edg = str(input("Give edge(say done when done): "))
        if edg != "done":
            weight = int(input("What is the edges weight?: "))
            edges.append(edge(edg[0],edg[1],weight))
        else:
            flag = False
            prim(edges, vertices)

runprim()