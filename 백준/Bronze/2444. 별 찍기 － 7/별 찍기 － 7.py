N = int(input())

blank = N

for i in range(1,2*N,2) :
    blank -= 1
    print(' ' * blank,end='')
    star = i
    print('*' * star)

for i in range(2*N-3,0,-2):
    print(' ' * blank,end=' ')
    blank += 1
    star = i
    print('*' * star)
