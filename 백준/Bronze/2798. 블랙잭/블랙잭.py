N, M = map(int, input().split())
Card = list(map(int, input().split()))
total = 0

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            SumOfCards = Card[i] + Card[j] + Card[k]
            if SumOfCards <= M and SumOfCards > total:
                total = SumOfCards

print(total)
