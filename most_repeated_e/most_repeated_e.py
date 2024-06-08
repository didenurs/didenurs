n = int(input("How many words are you going to enter?"))
words = []
scores = []
print("Enter the words.")

for i in range(n):
    word = str(input(""))
    words.append(word)

def most_letter():
    score = 0
    for kel in words:
        for j in range(len(kel)):
            if kel[j] == "e" or kel[j] == "E":
                score += 1
        scores.append(score)
        score = 0

most_letter()
x = max(scores)
print(words[scores.index(x)])