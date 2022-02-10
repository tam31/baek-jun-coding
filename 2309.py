a=[]
for i in range(9):
    a.append(int(input()))

re2 = 0
re=sum(a)
for i in range(9):
    for j in range(i+1, 9):
        re2 = re - (a[i]+a[j])
        if re2 == 100:
            a.remove(a[i])
            a.remove(a[j-1])
            break
    if sum(a) == 100:
        break
a.sort()
for i in range(7):
    print(a[i])
