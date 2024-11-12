A, B, V = map(int, input().split())

# 목표에 도달하는 마지막 날은 미끄러지지 않으므로 V - A까지 이동한 후, 마지막으로 A만큼 올라가야 함
distance_per_day = A - B

# 올림 처리: (V - A + distance_per_day - 1) // distance_per_day로 계산
d_count = (V - A + distance_per_day - 1) // distance_per_day + 1

print(d_count)
