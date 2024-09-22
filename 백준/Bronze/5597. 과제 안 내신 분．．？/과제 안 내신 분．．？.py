import sys
input = sys.stdin.readline

# 출석부를 False로 초기화합니다. 1번부터 30번까지, 0번 인덱스는 사용하지 않습니다.
atd_sub = [False] * 31

# 30명의 출석 정보를 입력받습니다.
for i in range(28):
    A = int(input())
    atd_sub[A] = True  # 해당 번호를 True로 설정하여 출석 처리
    
# 출석하지 않은 번호를 확인하고 출력합니다.
for i in range(1, 31):  # 1번부터 30번까지 확인
    if not atd_sub[i]:  # False인 경우, 즉 출석하지 않은 경우
        print(i)
