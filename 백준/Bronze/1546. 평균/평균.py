import sys
input = sys.stdin.readline

N = int(input())

# 점수 입력받기
S = list(map(int,input().split()))

max = -1

#최댓값 구하기
for i in range(N):
    if S[i] > max :
        max = S[i]
        
scores = 0

#조작 점수 만들고 전체 점수 구하기
for i in range(N):
    S[i] = S[i] / max * 100
    scores += S[i]
    
print(scores/N)

    
