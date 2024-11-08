N = int(input())

room = [1]
i = 0

while room[i] < N:
    i += 1
    next_room = room[i-1] + 6 * i 
    room.append(next_room)

print(i + 1)
