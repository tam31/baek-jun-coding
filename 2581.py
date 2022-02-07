a=int(input())
b=int(input())
num=[]
for i in range(a, b+1):
    count = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0 :
                count += 1
                break
        if count == 0:
            num.append(int(i))
if len(num) >0:
    print(sum(num))
    print(min(num))
else:
    print(-1)
        
