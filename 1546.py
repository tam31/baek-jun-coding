a=int(input())
b = list(map(int, input().split()))
c=max(b)
sum = 0
print(c)
for i in range(a):
   
    b[i] = b[i]/c*100
    print(b[i])
    sum +=b[i]
print(sum/a)
