N = int(input())

a = 0

for i in range (N):
    s = str(i)
    num = i
    for j in range(len(s)):
        num += int(s[j])
    if num == N :
        a = i
        break

print(a)