N, M = map(int, input().split())
board = [input() for _ in range(N)]

pattern1 = [[('W' if (i + j) % 2 == 0 else 'B') for j in range(8)] for i in range(8)]
pattern2 = [[('B' if (i + j) % 2 == 0 else 'W') for j in range(8)] for i in range(8)]

min_changes = float('inf')

for i in range(N - 7):
    for j in range(M - 7):
        changes1 = changes2 = 0
        for x in range(8):
            for y in range(8):
                if board[i + x][j + y] != pattern1[x][y]:
                    changes1 += 1
                if board[i + x][j + y] != pattern2[x][y]:
                    changes2 += 1
        min_changes = min(min_changes, changes1, changes2)

print(min_changes)
