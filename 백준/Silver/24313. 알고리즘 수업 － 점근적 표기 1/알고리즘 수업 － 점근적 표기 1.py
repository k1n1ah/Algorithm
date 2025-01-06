a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

condition = True

for n in range(n0, 1001):
    if a1*n + a0 > c * n :
        condition = False
        break

if condition :
    print(1)
else :
    print(0)