N = [[0 * 100 for _ in range(100)] for _ in range(100)]

P = int(input())
count = 0


for _ in range(P):
    A,B = map(int,input().split())
    for i in range(10):
        for j in range(10):
            if N[A+i][B+j] != 1 :
                N[A+i][B+j] = 1
                count += 1
            else :
                continue

print(count)