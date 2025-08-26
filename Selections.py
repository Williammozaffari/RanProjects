import random
import math

# We define a class called chromosome to represent the population.
class chromosome:
    def __init__(self, genes, fit):
        self.genes = []
        self.fit = 0

# Here are the different algorithms for selecting population from the current generation for a new generation. 
def ranselect(gen):
    pop = len(gen)
    newgen = []
    for i in range(pop):
        newgen.append(random.choice(gen))
    return newgen

def perportional(gen):
    total = 0
    pop = len(gen)
    for i in range(pop):
        total = gen[i].fit
    w = [(i.fit/total) for i in gen]
    newgen = random.choices(gen, weights = w, k = pop)
    return newgen

def valuer(chrom):
    return chrom.fit

def rank_based(gen):
    pop = len(gen)
    ranking = gen
    ranking.sort(reverse = True, key = valuer)
    newgen = random.choices(ranking, weights = [i+1 for i in range(pop)], key = pop)
    return newgen

def tournament(gen, t):
    pop = len(gen)
    newgen = []
    for i in range(pop):
        group = random.choices(gen, weights = None, key = t)
        group.sort()
        newgen.append(group[0])
    return newgen

def truncation(gen, t):
    pop = len(gen)
    ranking = gen.sort(reversed = False, key = valuer)
    edge = t/100
    upper = math.ceil(edge*pop)
    selection = [ranking[i] for i in range(upper)]
    newgen = random.choices(selection, weights = None, key = pop)
    return newgen


    size = len(chrom1.genes)
    point1 = random.randint(0, size-1)
    flag = True
    while flag:
        point2 = random.randint(0, size-1)
        if point1 != point2:
            flag = False
    a = min(point1, point2)
    b = max(point1, point2)
    newchrom1 = chrom1.genes[0:a] + chrom2.genes[a:b] + chrom1.genes[b:size]
    newchrom2 = chrom2.genes[0:a] + chrom1.genes[a:b] + chrom2.genes[b:size]
    return newchrom1, newchrom2




