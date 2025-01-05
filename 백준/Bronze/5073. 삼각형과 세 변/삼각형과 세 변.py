while True:
    a1, a2, a3 = map(int, input().split())
    if a1 == 0 and a2 == 0 and a3 == 0:
        break
    sides = [a1, a2, a3]
    sides.sort()  
    if sides[2] >= sides[0] + sides[1]:  
        print("Invalid")
    else:
        if a1 == a2 == a3:
            print("Equilateral")
        elif a1 == a2 or a1 == a3 or a2 == a3:
            print("Isosceles")
        else:
            print("Scalene")
