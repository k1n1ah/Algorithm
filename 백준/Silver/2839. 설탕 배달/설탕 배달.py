N= int(input())
nums = []

for i in range(N//5 + 1):
    if (N - i* 5) % 3 == 0 :
        r = (N-i*5) // 3
        nums.append(i + r)

if nums :
    print(min(nums))
else:
    print(-1)