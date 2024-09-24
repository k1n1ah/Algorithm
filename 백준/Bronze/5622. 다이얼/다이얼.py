S = input()
A = 0
dial = ['ABC', 'DEF', 'GHI', 'JKL','MNO', 'PQRS','TUV','WXYZ']

for char in S:
    for i in range(len(dial)):
        if char in dial[i]:
            A += (i+2) + 1
            break

print(A)