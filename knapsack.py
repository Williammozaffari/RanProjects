
def fKnapsack(values, weights, cap):
    eco = []
    for i in range(len(values)):
        eco.append(values[i]/weights[i])
    sorted = eco.copy()
    sorted.sort(reverse = True)
    bag = []
    profit = 0
    flag = True
    while flag:
        current = eco.index(sorted[0])
        if cap >= weights[current]:
            cap -= weights[current]
            profit += values[current]
            bag.append(f"|obj: {current}, frac: 1|")
            sorted.pop(0)
        else:
            if cap == 0:
                flag = False
            else:
                frac = cap/weights[current]
                profit += values[current]*frac
                cap = 0
                bag.append(f"|obj: {current}, frac: {frac}")
    print(bag)
    print(f"Gained profit: {profit}$")

    
def kanpsack01(values, weights, cap):
    eco = []
    for i in range(len(values)):
        eco.append(values[i]/weights[i])
    sorted = eco.copy()
    sorted.sort(reverse = True)
    bag = []
    profit = 0
    flag = True
    while flag:
        if (cap == 0) or (len(sorted) == 0):
            flag = False
        else:
            current = eco.index(sorted[0])
            if cap >= weights[current]:
                bag.append(current)
                cap -= weights[current]
                profit += values[current]
            sorted.pop(0)
    print(f"Selected objects are: {bag}")
    print(f"Gained profit: {profit}")

kanpsack01([10,10,19],[1,2,3],3)
