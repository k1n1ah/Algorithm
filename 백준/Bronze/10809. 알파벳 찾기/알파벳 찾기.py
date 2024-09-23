S = input()
A = [-1] * 26 
for i in range(len(S)):
    index = ord(S[i])-ord('a')
    if A[index] == -1:
        A[index] = i
       
for i in range(len(A)):
    print(A[i],end=' ')