import heapq

n = int(input())
data = []
for i in range(n):
    heapq.heappush(data, int(input()))

sum2 = 0
while len(data) != 1:
    one = heapq.heappop(data)
    two = heapq.heappop(data)
    sum = one + two
    heapq.heappush(data, sum)
    sum2 += sum
print(sum2)
