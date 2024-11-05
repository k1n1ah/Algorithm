N, B = map(str, input().split())
N = int(N)
B = int(B)
A = list()

while True:
    if N < B:
        if N < 10:
            A.append(N)
        else:
            k = ord('A') + (N - 10)
            A.append(chr(k))
        break
    else:
        r = N % B
        if r < 10:
            A.append(r)
        else:
            k = ord('A') + (r - 10)
            A.append(chr(k))
        N = N // B

for i in A[::-1]:
    print(i, end='')
