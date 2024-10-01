# N과 M 입력받기
N, M = map(int, input().split())

# 0으로 초기화된 N x M 크기의 2차원 리스트 A와 B 생성
A = [[0] * M for _ in range(N)]
B = [[0] * M for _ in range(N)]

# A 배열 입력받기
for i in range(N):
    Num = list(map(int, input().split()))
    for j in range(M):
        A[i][j] = Num[j]

# B 배열 입력받기
for i in range(N):
    Num = list(map(int, input().split()))
    for j in range(M):
        B[i][j] = Num[j]

# A와 B 더하기
C = [[A[i][j] + B[i][j] for j in range(M)] for i in range(N)]

# 결과 출력
for i in range(N):
    for j in range(M):
        print(C[i][j], end=' ')
    print()
