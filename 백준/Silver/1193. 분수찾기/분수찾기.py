N = int(input())
count = 1
a , b = 1, 1

while N > count :
    N -= count
    count += 1

#count가 짝수면
if count % 2 == 0:
    a = 1
    b = count
    for i in range(N-1):
        a += 1
        b -= 1
#count가 홀수면
else :
    a = count
    b = 1
    for i in range(N-1):
        a -= 1
        b += 1

print(f"{a}/{b}")

