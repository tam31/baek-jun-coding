n,m = map(int, input().split())
num = list(map(int, input().split()))

re=[]
for i in range(n):
    for j in range(i+1, n):
        for z in range(j+1, n):
            if num[i]+num[j]+num[z] > m:
                continue
            else:
               re.append(num[i]+num[j]+num[z])

print(max(re))
