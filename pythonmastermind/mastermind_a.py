def compare_code(proposal, secret_code):
    proposal = str(proposal)
    secret_code = str(secret_code)
    correct_pos = 0
    incorrect_pos = 0
    found = [False] * len(secret_code)

    for idx_secret, digit_secret in enumerate(secret_code):
        if digit_secret == proposal[idx_secret]:
            correct_pos += 1
            found[idx_secret] = True
            continue
        for idx_proposal, digit_proposal in enumerate(proposal):
            if not found[idx_proposal] and digit_proposal == digit_secret:
                incorrect_pos += 1
                found[idx_proposal] = True
                break

    return (correct_pos, incorrect_pos)


def create_list(n):
    return list(range(10 ** (n - 1), 10 ** n))


def guess(listProposal, result):
    ret = []
    for i in listProposal[1:]:
        if compare_code(listProposal[0], i) == result:
            ret.append(i)
    return ret


Right_place = []
Wrong_place = []
Guesses = []

n = 6
secret_code = 508725
# n = 4
# secret_code = 2963
listProposal = create_list(n)

while len(listProposal) != 0:
    proposal = listProposal[0]
    result = compare_code(proposal, secret_code)
    print(proposal)
    Guesses.append(proposal)
    Right_place.append(result[0])
    Wrong_place.append(result[1])
    if result == (n, 0):
        print("Found the secret code", proposal)
        break
    listProposal = guess(listProposal, result)

print("Guess list: ", Guesses)
print("# of digits in correct position:   ", Right_place)
print("# of digits in incorrect position: ", Wrong_place)
