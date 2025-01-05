N = int(input())
x = []
y = []

for i in range(N):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
if N == 1: 
    print(0)
else:
    width = max(x) - min(x)
    height = max(y) - min(y)
    print(width * height)
