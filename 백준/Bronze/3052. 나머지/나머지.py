import sys
input = sys.stdin.readline

remainder = [False] * 42
count = 0

for i in range(10):
    N = int(input())
    M = N % 42
    remainder[M] = True
    
for i in range(42):
    if remainder[i] == True :
        count += 1
        
print(count)