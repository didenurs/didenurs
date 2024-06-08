# listedeki sayıları küçükten büyüğe sırala

def BubbleSort(list):
    swapped = True

    while (swapped):
        swapped = False

        for i in range(0, len(list)-1):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                swapped = True
    return list

listA = [-99, 758, 9, -37, 0]
BubbleSort(listA)
print(listA)

