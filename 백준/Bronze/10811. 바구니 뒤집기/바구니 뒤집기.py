import sys
input = sys.stdin.readline

# 바구니의 갯수와 횟수 입력
N, M = map(int, input().split())

# 바구니 번호 초기화 (1~N)
A = list(range(1, N+1))

# M번 동안 역순으로 뒤집기
for _ in range(M):
    i, j = map(int, input().split())
    # i번 바구니부터 j번 바구니까지 역순으로 뒤집기
    A[i-1:j] = reversed(A[i-1:j])  # 슬라이싱을 사용하여 부분 리스트를 뒤집음

# 바구니 출력
for i in range(1, N+1):
    print(A[i-1], end=' ')
