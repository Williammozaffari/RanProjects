import heapq



class edge:
    def __init__(self,p1,p2,w):
        self.p1 = p1
        self.p2 = p2
        self.w = w
    def __repr__(self):
        return(f"{self.p1}{self.p2}")
    
class vertex:
    def __init__(self,name):
        self.name = name
        self.parent = None
        self.key = None
    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
    def __repr__(self):
        return(self.name)


def prim(e, v):
    vertices = {vert.name: vert for vert in v}
    if not vertices:
        return []
    for vert in vertices.values():
        vert.key = float('inf')
        vert.parent = None
    start = v[0].name
    vertices[start].key = 0

    visited = set()
    pq = [(0, start)] 

    while pq:
        key, u = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)

        # relax outgoing edges from u
        for ed in e:
            if ed.p1 == u and ed.p2 not in visited:
                if ed.w < vertices[ed.p2].key:
                    vertices[ed.p2].key = ed.w
                    vertices[ed.p2].parent = u
                    heapq.heappush(pq, (ed.w, ed.p2))
            elif ed.p2 == u and ed.p1 not in visited:
                if ed.w < vertices[ed.p1].key:
                    vertices[ed.p1].key = ed.w
                    vertices[ed.p1].parent = u
                    heapq.heappush(pq, (ed.w, ed.p1))

    mst = []
    for name, vert in vertices.items():
        if vert.parent is not None:
            a, b = sorted([name, vert.parent])
            mst.append(a + b)
    mst.sort()
    return mst

def runprim():
    alpha = "abcdefghijklmnopqrstuvwxyz"
    size = int(input("How many vertices?(max 26): "))
    vertices = []
    edges = []
    for i in range(size):
        vertices.append(vertex(alpha[i]))
    flag = True
    while flag:
        edg = str(input("Give edge(say done when done): "))
        if edg != "done":
            weight = int(input("What is the edges weight?: "))
            edges.append(edge(edg[0],edg[1],weight))
        else:
            flag = False
            print(prim(edges, vertices))

runprim()
