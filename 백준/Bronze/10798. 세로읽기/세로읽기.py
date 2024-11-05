W = [['' * 15 for _ in range(15)] for _ in range(5)]

for i in range(5):
    Words = input()
    for j in range(len(Words)):
        W[i][j] = Words[j]

for j in range(15):
    for i in range(5):
        if W[i][j] != '':
            print(W[i][j], end='')
        else:
            continue