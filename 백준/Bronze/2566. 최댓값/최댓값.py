# 2차원 9*9 행렬 만들기
N = [[0] * 9 for _ in range(9)]

a, b = 0, 0
max = -1
for i in range(9):
    A = list(map(int, input().split()))
    for j in range(9):
        K = A[j]
        N[i][j] = K
        if K > max:
            max = K
            a = i + 1
            b = j + 1

print(max)
print(a, b)