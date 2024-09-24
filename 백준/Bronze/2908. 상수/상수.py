A, B = map(str, input().split())

nA = 0
nB = 0

for i in range(len(A)):
    nA += int(A[i]) * pow(10, i)
    nB += int(B[i]) * pow(10, i)

if nA > nB:
    print(nA)
else:
    print(nB)