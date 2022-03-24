n,m = map(int, input().split())
data = list(map(int, input().split()))

start = 0
end = max(data)

re = 0
while start<= end:
    mid = (start+end) // 2
    total = 0
    for i in data:
        if i < mid :
            continue
        else:
            total += i - mid

    if total < m:
        end = mid -1
    else:
        re = mid
        start = mid +1
    
print(re)


        
