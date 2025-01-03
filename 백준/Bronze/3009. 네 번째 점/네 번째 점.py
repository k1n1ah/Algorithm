cx = []
cy = []


for i in range(3):
    x1, y1 = map(int, input().split())
    cx.append(x1)
    cy.append(y1)

x = cx[0]
y = cy[0]

if x != cx[1] :
    if x == cx[2] :
        x = cx[1]
else :
    x = cx[2]

if y != cy[1] :
    if y == cy[2] :
        y = cy[1]
else :
    y = cy[2]


print(x,y)