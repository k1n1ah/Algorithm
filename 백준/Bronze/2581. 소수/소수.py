M = int(input())
N = int(input())

total = 0
min_prime = 0

for i in range(M,N+1) :
    if i < 2 :
        continue
    else :
        check = True
        j = 2
        while check :
            if j == i :
                break
            if i % j == 0 :
                check = False
                break
            j += 1
        if check :
            total += i
            if min_prime == 0 :
                min_prime += i

if total > 0 :
    print(total)
    print(min_prime)
else :
    print(-1)