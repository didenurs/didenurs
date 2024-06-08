def Avg(list):
    sum = 0

    for i in range(len(list)-1):
        sum += list[i]
    return sum/len(list)

list = [13, 17, 24, 33]
Avg = Avg(list)
print(Avg)
