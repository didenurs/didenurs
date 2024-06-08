import random

def make_a_guess(secret_list,pos_score,neg_score):
    # neg_score = 0
    # pos_score = 0
    guess = random.randint(10**(n-1), 10**n-1)
    #print(guess)
    guess_list = [int(x) for x in str(guess)]

    for i in range(len(guess_list)):

        if secret_list[i] == guess_list[i]:
            pos_score += 1
            kontrol_list[i] = True


    for j in range(len(guess_list)):
        k = 0
        while k < (len(secret_list)):
            if j != k and kontrol_list[k] == False:
                #print("j:", j, "k:", k)
                if guess_list[j] == secret_list[k]:
                    neg_score += 1
                    break
            k = k+1

    #print("pos:", pos_score, "neg:", neg_score)

    if neg_score >= pos_score:
        neg_score = neg_score-pos_score

    pos_list.append(pos_score)
    neg_list.append(neg_score)
    tahminler.append(guess)

    print("positive score=", pos_list)
    print("negative score=", neg_list)
    print("tahminler=", tahminler)

    return pos_score,neg_score, guess

n = int(input("basamak sayisini giriniz: \n"))
secret_code = random.randint(10**(n-1), 10**n-1)
#secret_code = int(input("sectiginiz basamak sayisinda bir secret kod giriniz: "))
print(secret_code)

secret_list = [int(x) for x in str(secret_code)]

guess = -1

pos_list = []
neg_list = []
tahminler = []
kontrol_list = [False for i in range(n)]
pos_score = 0

while pos_score != 1:

    pos_score, neg_score, guess = make_a_guess(secret_list,0,0)

    if pos_score == 1:     # 1 tane pozitif skor bulduktan sonra pozitifin hangi digit olduğu bulunacak
        print("secret code: ", secret_code, " guess: ", guess)
        break

x = [int(a) for a in str(guess)]
for i in range(n):
    print(x[i])




if secret_code == guess:
    print("computer found the secret code:", secret_code)