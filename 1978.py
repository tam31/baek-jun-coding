num = int(input())

re = 0
a=list(map(int, input().split()))
for i in range(num):
    count = 0
    for j in range(2, a[i]+1):
        if a[i] % j == 0 and a[i]!=1:
            count += 1
    if count == 1:
        re +=1
print(re)
        
