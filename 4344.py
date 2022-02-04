num1 = int(input())
for j in range(num1):
    a= list(map(int, input().split()))
    num=a.pop(0)
    avg=sum(a)/num
    count = 0
    for i in range(num):
        if avg< a[i]:
            count+=1
    print("%.3f" %(count*(100/num))+'%')
