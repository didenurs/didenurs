# find recursive average

def recursive_ave(sum,n):
    new_num = int(input())
    if new_num == -1:
        return sum/n
    else:
        return recursive_ave(sum+new_num,n+1)

print(recursive_ave(0,0))