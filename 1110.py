a=int(input())
b=a
c=0
d=0
count=0

while True:
   c=(b//10)+(b%10)
   d=(b%10)*10+(c%10)
   b = d
   if d == a:
        break
    else:
        count +=1
    
print(count)
