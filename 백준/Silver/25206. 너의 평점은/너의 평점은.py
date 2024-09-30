# 학점과 점수를 딕셔너리로 매핑
grade_to_score = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0
}

score = 0
total_credit = 0

for _ in range(20):
    Name, credit, grade = map(str, input().split())
    credit = float(credit)  # 학점은 float로 변환
    
    # 해당 학점에 해당하는 점수를 딕셔너리에서 가져옴
    if grade in grade_to_score:
        total_credit += credit
        score += credit * grade_to_score[grade]

# 평균 학점 계산
final_score = score / total_credit
print(f"{final_score:.6f}")
