class edge:
    def __init__(self,p1,p2,w):
        self.p1 = p1
        self.p2 = p2
        self.w = w
    def __str__(self):
        print(f"{self.p1}{self.p2}")




def kruskal(e, v):
    path = []
    e.sort(key = lambda edge: edge.w)
    for i in e:
        set1 = next(s for s in v if i.p1 in s)
        set2 = next(s for s in v if i.p2 in s)
        if set1 != set2:
            v.remove(set1)
            v.remove(set2)
            set1.extend(set2)
            v.append(set1)
            path.append(f"{i.p1}{i.p2}")
    print(path)
        
    
def runkruskal():
    alpha = "abcdefghijklmnopqrstuvwxyz"
    size = int(input("How many vertices?(max 26): "))
    vertices = []
    edges = []
    for i in range(size):
        vertices.append([alpha[i]])
    flag = True
    while flag:
        edg = str(input("Give edge(say done when done): "))
        if edg != "done":
            weight = int(input("What is the edges weight?: "))
            edges.append(edge(edg[0],edg[1],weight))
        else:
            flag = False
            kruskal(edges, vertices)

runkruskal()