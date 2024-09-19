import sys
input = sys.stdin.readline

num = 0;
max = 0
for i in range(9):
    A = int(input())
    if(A > max):
        max = A
        num = i+1
        
        
print(max)
print(num)