N = int(input())

count = 0
for _ in range(N):
    S = input()
    A = []  # 이미 확인된 문자를 저장할 리스트
    group = True

    # 길이가 1인 단어는 무조건 그룹 단어로 간주
    if len(S) == 1:
        count += 1
        continue  # break 대신 continue로 현재 단어 처리 후 다음 단어로 넘어감

    i = 0
    while i < len(S):
        if S[i] not in A:  # 처음 등장하는 문자
            A.append(S[i])
        else:  # 이미 등장한 문자가 다시 나왔으면 그룹 단어가 아님
            group = False
            break

        # 연속된 동일 문자는 건너뛰기
        while i + 1 < len(S) and S[i] == S[i + 1]:
            i += 1

        i += 1  # 다음 문자로 이동

    if group:  # 그룹 단어인 경우 카운트 증가
        count += 1

print(count)
