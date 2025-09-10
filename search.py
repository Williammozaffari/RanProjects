def binarysearch(list, obj):
    p1 = 0
    p2 = len(list)-1
    result = None
    flag = True
    while flag:
        mid = (p1 + p2)//2
        if list[mid] == obj:
            result = mid
            flag = False
        elif list[mid] > obj:
            p2 = mid
        else:
            p1 = mid
    print(f"object is at index {result}")
    return


