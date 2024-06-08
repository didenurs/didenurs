import random

n = int(input("lütfen basamak sayısını giriniz: \n"))
secret_code= random.randint(10**(n-1), 10**n-1)
print(secret_code)


secret_list = [int(x) for x in str(secret_code)]

#print(secret_list[0])

guess_num = -1

pos_list = []
neg_list = []
tahminler = []
kontrol_list = [False for i in range(n)]

while secret_code != guess_num:
    guess_num = int(input("tahmin: "))
    guess_list = [int(x) for x in str(guess_num)]
    pos_score = 0
    neg_score = 0

    print(guess_list)

    for i in range(len(guess_list)):
        #print(guess_list[i])

        if secret_list[i] == guess_list[i]:
            pos_score += 1
            kontrol_list[i] = True


    for j in range(len(guess_list)):
        k = 0
        while k < (len(secret_list)):
            if j != k and kontrol_list[k]==False:
                print("j:",j,"k:",k)
                if guess_list[j] == secret_list[k]:
                    neg_score += 1
                    break
            k = k+1

    print("pos:", pos_score, "neg:", neg_score)

    if neg_score >= pos_score:
        neg_score = neg_score-pos_score

    pos_list.append(pos_score)
    neg_list.append(neg_score)
    tahminler.append(guess_num)

    print("positive score=", pos_list)
    print("negative score=", neg_list)
    print("tahminler=", tahminler)

    if secret_code == guess_num:
        print("you found the secret code:", secret_code)
        break