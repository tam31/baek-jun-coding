import sys
k, n = map(int,sys.stdin.readline().split())
data = []
for i in range(k):
    data.append(int(sys.stdin.readline()))

start = 1
end = max(data)

re = 0

while start <= end:
    total = 0
    mid = (start+end) // 2
       
    for i in data:
        '''
        나누기여서 필요없음
        if mid > i:
            continue
        else:
        '''
        total += i//mid
    if total < n:
        end = mid -1
    else:
        re = mid
        start = mid + 1

print(re)
                
