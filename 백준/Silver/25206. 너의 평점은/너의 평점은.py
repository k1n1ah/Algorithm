from pickletools import long4

score = 0
total_credit = 0
for _ in range(20):
    Name, credit, grade = map(str, input().split())
    if grade == "A+":
        total_credit += float(credit)
        score +=  float(credit) * 4.5
    elif grade == "A0":
        total_credit += float(credit)
        score +=  float(credit) * 4.0
    elif grade == "B+":
        total_credit += float(credit)
        score +=  float(credit) * 3.5
    elif grade == "B0":
        total_credit += float(credit)
        score +=  float(credit) * 3.0
    elif grade == "C+":
        total_credit += float(credit)
        score +=  float(credit) * 2.5
    elif grade == "C0":
        total_credit += float(credit)
        score +=  float(credit) * 2.0
    elif grade == "D+":
        total_credit += float(credit)
        score +=  float(credit) * 1.5
    elif grade == "D0":
        total_credit += float(credit)
        score +=  float(credit) * 1.0
    elif grade == "F" :
        total_credit += float(credit)
        score +=  float(credit) * 0.0
    else :
        continue

final_score = score/ total_credit
print("{:6f}".format(final_score))