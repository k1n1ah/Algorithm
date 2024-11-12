A, B, V = map(int, input().split())

# 목표에 도달하는 마지막 날은 미끄러지지 않으므로 V - A까지 이동한 후, 마지막으로 A만큼 올라가야 함
distance_per_day = A - B

# 목표 전날의 거리 V - A
# (V-A) / distance_per_day 를 해서 나머지가 0이 되면 좋지만 아닌 경우
# 거리를 순수 이동 거리로 나눴을때 나머지값이 무시되어버림
# 그래서 나눗셈을 할 distance_per_day만큼 올려준다음
# -1을 해서 올림 처리를 해줌 
# 그리고 전체에서 +1을 해서 마지막날을 더해줌
d_count = (V - A + distance_per_day - 1) // distance_per_day + 1

print(d_count)
