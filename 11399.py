a= int(input())
time = list(map(int, input().split()))
time.sort()
re = 0
sum = 0
for i in range(a):
    re += time[i]
    sum += re
print(sum)
