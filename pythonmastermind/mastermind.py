import random

n = int(input("lütfen basamak sayısını giriniz: \n"))
secret_code= random.randint(10**(n-1), 10**n-1)
print(secret_code)


secret_list = [int(x) for x in str(secret_code)]

print(secret_list[0])

guess_num = int(input("tahmin: "))
guess_list = [int(x) for x in str(guess_num)]
pos_score = 0
neg_score = 0
neg_score_total = 0
pos_list = []
neg_list = []
tahminler = []
print(guess_list)

for i in range(len(guess_list)):
    print(guess_list[i])

    if secret_list[i] == guess_list[i]:
        pos_score += 1


for j in range(len(secret_list)):
    for k in range(len(guess_list)):
        if j != k:
            if secret_list[j] == guess_list[k]:
                 neg_score += 1

    #    print("j=", j, "k=",k+1)
        # if secret_list[j] == guess_list[k]:
        #     neg_score += 1

pos_list.append(pos_score)
neg_list.append(neg_score)
tahminler.append(guess_num)
print("positive score=", pos_list)
print("negative score=", neg_list)
print("tahminler=", tahminler)
# size = len(guess_list)
# print(size)





