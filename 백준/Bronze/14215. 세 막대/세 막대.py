a,b,c = map(int,input().split())

sides = sorted([a, b, c])

if sides[2] >= sides[0] + sides[1]:
    sides[2] = sides[0] + sides[1] - 1
    
print(sum(sides))