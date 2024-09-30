S = input()
A = ["c=", "c-","dz=","d-","lj","nj","s=","z="]
count = 0
for word in A :
        count += S.count(word)
        S = S.replace(word,' ') #남은 알파벳들이 모여서 A에 있는 문자를 만들수도 있으므로 
print(count + len(S.replace(' ', '')))
        
    