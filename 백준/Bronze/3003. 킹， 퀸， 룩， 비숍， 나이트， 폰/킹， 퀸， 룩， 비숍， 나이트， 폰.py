#킹 1/ 퀸 1/ 룩 2/ 비숍 2/ 나이트 2/ 폰 8

A = [1,1,2,2,2,8]

S = [int(x) for x in input().split()]

for i in range(len(A)) :
    print(A[i] - S[i], end=' ')

