n = int(input("How many words are you going to enter?"))
# words = ["Pumpkin", "aarDvaRK", "heLLo", "naPkin", "purple"]
a = []
c = []
print("Enter the words.")

for i in range(n):
    words = str(input(""))
    a.append(words)
    c.append(words.lower())
 min = ord(c[0][0])
for i in range (len(a)):
    if ord(c[i][0]) < min:
        min = ord(c[i][0])
        key = i

print(min)
print("The first word alphabetically is" + min)




# for i in range(n):
#     if words[i][0].isupper():
#         words[i] = words[i].lower()
#
# #print(words)
#
# while True:
#     first = []
#     second = []
#
#     for i in range(n):
#         first.append(ord(words[i][0]))
#
#     min1 = min(first)
#     min_values = [i for i, x in enumerate(first) if x == min1]
#
#     if len(min_values) > 1:
#         for j in min_values:
#             second.append(ord(words[j][1]))
#
#         min2 = min(second)
#         second_index = second.index(min2)
#         print(words[second_index])
#         words.remove(words[second_index])
#         n -= 1
#
#     else:
#         next_index = first.index(min1)
#         print(words[next_index])
#
#         words.remove(words[next_index])
#         n -= 1
#
#     if len(words) == 0:
#         break