import sys
input = sys.stdin.readline

N,M = map(int,input().split())
A = list(range(1, N+1))
    
for _ in range(M):
    i,j = map(int, input().split())
    temp = A[i-1];
    A[i-1] = A[j-1]
    A[j-1] = temp

for i in range(N):
    print(A[i], end =' ')