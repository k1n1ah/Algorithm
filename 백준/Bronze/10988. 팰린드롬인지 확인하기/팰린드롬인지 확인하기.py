S = input()
N = True
for i in range(len(S)) :
        j = len(S)-1-i
        if S[i] != S[j] :
            N = False
            
if N == True :
    print(1)
else :
    print(0)
    