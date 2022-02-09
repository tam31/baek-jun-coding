a, b = map(int, input().split())
num=[]
cnt=0
for i in range(a):
    num.append(int(input()))
for j in range(a-1, -1 ,-1):
    cnt += b // num[j]
    b = b % num[j]
print(cnt)
