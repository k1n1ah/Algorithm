S = input()
A = ["c=","c-","dz=","d-","lj","nj","s=","z="]
count = 0

for word in A:
    count += S.count(word)  # 패턴이 몇 번 나오는지 센다
    S = S.replace(word, " ")  # 찾은 패턴을 제거

print(count + len(S.replace(" ", "")))  # 남은 문자도 추가
