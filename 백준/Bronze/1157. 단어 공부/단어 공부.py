S = input()

Cap = [0] * (ord('Z') - ord('A')+1)

for i in S:
    Q = i.upper()
    Cap[ord(Q) - ord('A')] += 1

max = 0
index = 0
count = 0

for i in range(len(Cap)) :
    if Cap[i] > max:
        max = Cap[i]
        count = 1
        index = i
    elif max == Cap[i]:
        count += 1

if count == 1 :
    print(chr(index + ord('A')))
else:
    print("?")