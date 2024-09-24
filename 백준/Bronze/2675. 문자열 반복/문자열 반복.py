T = int(input())

for _ in range(T):
    R, S = map(str, input().split())
    R = int(R)
    for i in range(len(S)):
        count = 0
        while count < R:
            print(S[i], end='')
            count += 1
        count = 0
    print()  

