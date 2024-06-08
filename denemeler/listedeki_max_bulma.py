# listedeki maxi bul

listA = [-99, 758, 9, -37, 0]

def Max(list):
    max = list[0]
    for i in range(len(list)):
        if max < list[i]:
            max = list[i]
    print(max)
    return max

Max(listA)