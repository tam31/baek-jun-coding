a,b,c=map(int, input().split())

count=1
while c-a>0:
    c+=b
    count +=1
    c-=a
print(count)
