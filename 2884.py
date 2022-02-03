a,b = map(int, input().split())
if b-45<0:
    if int(a)-1 <0:
        a = 23
    else:
        a-=1
    b = b+60-45
else:
    b = b-45
print(a, b)
