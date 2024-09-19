import sys
input = sys.stdin.readline

N = int(input())

A = list(map(int,input().split()))

max = -1000001;
min = 1000001;

for i in A :
    if i < min:
        min = i
    if i > max:
        max = i
        
print(min,max)
    