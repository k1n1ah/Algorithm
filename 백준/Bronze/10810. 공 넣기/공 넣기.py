import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [0] * N  

for _ in range(M):
    i, j, k = map(int, input().split())
    for num2 in range(i-1, j): 
        A[num2] = k

for value in A:
    print(value, end=' ')
