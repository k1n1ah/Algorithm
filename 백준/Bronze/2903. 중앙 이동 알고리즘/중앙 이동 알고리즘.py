N = int(input())

dots = 2
count = 1

for i in range(N) :
    dots = dots + pow(2,count-1)
    count += 1

print(pow(dots,2))
