import random

def random_guess_generate(n):
    guess = random.randint(10 ** (n - 1), 10 ** n - 1)
    guess_list = [int(x) for x in str(guess)]
    return (guess, guess_list)

def calculate_score(secret_list,guess):
    pos_score=0
    neg_score=0
    guess_list = [int(x) for x in str(guess)]

    for i in range(len(guess_list)):
        if secret_list[i] == guess_list[i]:
            pos_score += 1
            kontrol_list[i] = True

    for j in range(len(guess_list)):
        k = 0
        while k < (len(secret_list)):
            if j != k and kontrol_list[k] == False:
                if guess_list[j] == secret_list[k]:
                    neg_score += 1
                    break
            k = k+1

    if neg_score >= pos_score:
        neg_score = neg_score-pos_score

    pos_list.append(pos_score)
    neg_list.append(neg_score)
    tahminler.append(guess)

    return pos_score,neg_score

n = int(input("Please enter n (number of digits): \n"))
secret_code = int(input("Please enter the secret code: \n"))
secret_list = [int(x) for x in str(secret_code)]

if len(secret_list) != n:
    print("Your Entry is wrong. Please enter", n, "digits.")
    secret_code = int(input("Please enter the secret code: \n"))
    secret_list = [int(x) for x in str(secret_code)]

guess = -1
pos_list = []
neg_list = []
tahminler = []
kontrol_list = [False for i in range(n)]
pos_score = 0
sonuc = ["" for x in range(n)]
found = []

print("Computer is searching for the secret code, please wait........")
# 1 tane pozitif skor bul
while pos_score != 1:
    guess, guess_list = random_guess_generate(n)
    pos_score, neg_score = calculate_score(secret_list,guess)
    if pos_score == 1:
        break

# 1 tane pozitif skor bulduktan sonra pozitifin hangi sıradaki digit olduğu ve değeri bulunacak
y = [int(a) for a in str(guess)]

for g in range(n):
    org = y[g]
    if y[g] > 8:
        y[g] = 1
    else:
        y[g] = 9-y[g]

    sy = [str(i) for i in y]
    res = int("".join(sy))

    pos_score, neg_score = calculate_score(secret_list,res)
    if pos_score == 0:
        found.append(g)
        sonuc[g] = org
        break
    else:
        y[g] = org

if n > 1:
    for m in range(2, n+1):
        while pos_score != m:
            guess, guess_list = random_guess_generate(n)
            if m == 2:
                if guess_list[found[m-2]] == sonuc[found[m-2]]:
                    new_guess = guess
                    pos_score, neg_score = calculate_score(secret_list, new_guess)
                    if pos_score == m:
                         break
            if m == 3:
                if guess_list[found[m-2]] == sonuc[found[m-2]] and guess_list[found[m-3]] == sonuc[found[m-3]]:
                    new_guess = guess
                    pos_score, neg_score = calculate_score(secret_list, new_guess)
                    if pos_score == m:
                         break
            if m==4:
                if guess_list[found[m-2]] == sonuc[found[m-2]] and guess_list[found[m-3]] == sonuc[found[m-3]] and guess_list[found[m-4]] == sonuc[found[m-4]]:
                    new_guess = guess
                    pos_score, neg_score = calculate_score(secret_list, new_guess)
                    if pos_score == m:
                         break
            if m == 5:
                if guess_list[found[m - 2]] == sonuc[found[m - 2]] and guess_list[found[m - 3]] == sonuc[found[m - 3]] and \
                        guess_list[found[m - 4]] == sonuc[found[m - 4]] and guess_list[found[m - 5]] == sonuc[found[m - 5]]:
                    new_guess = guess
                    pos_score, neg_score = calculate_score(secret_list, new_guess)
                    if pos_score == m:
                        break
            if m == 6:
                if guess_list[found[m - 2]] == sonuc[found[m - 2]] and guess_list[found[m - 3]] == sonuc[found[m - 3]] and \
                        guess_list[found[m - 4]] == sonuc[found[m - 4]] and guess_list[found[m - 5]] == sonuc[found[m - 5]] and guess_list[found[m - 6]] == sonuc[found[m - 6]]:
                    new_guess = guess
                    pos_score, neg_score = calculate_score(secret_list, new_guess)
                    if pos_score == m:
                        break
            if m == 7:
                if guess_list[found[m - 2]] == sonuc[found[m - 2]] and guess_list[found[m - 3]] == sonuc[found[m - 3]] and \
                        guess_list[found[m - 4]] == sonuc[found[m - 4]] and guess_list[found[m - 5]] == sonuc[found[m - 5]] and guess_list[found[m - 6]] == sonuc[found[m - 6]] and guess_list[found[m - 7]] == sonuc[found[m - 7]]:
                    new_guess = guess
                    pos_score, neg_score = calculate_score(secret_list, new_guess)
                    if pos_score == m:
                        break

        y = [int(a) for a in str(new_guess)]

        for g in range(n):
            if g != found[m-2]:
                org = y[g]
                if y[g] > 8: y[g]=1
                else: y[g]=9-y[g]

                sy = [str(i) for i in y]
                res = int("".join(sy))

                pos_score, neg_score = calculate_score(secret_list, res)
                if pos_score==m-1:
                    found.append(g)
                    sonuc[g]=org
                    break
                else:
                    y[g]=org

if secret_code == guess:
    print("Computer found the secret code:", secret_code)
    print("Guess list:", tahminler[:-1])
    print("list of digits in correct position:", pos_list[:-1])
    print("list of digits in incorrect position:", neg_list[:-1])