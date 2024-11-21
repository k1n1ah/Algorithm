x,y,w,h = map(int, input().split())

print(min(abs(0-x),abs(w-x),abs(h-y),abs(0-y)))


