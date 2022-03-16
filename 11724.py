from collections import deque

n,m = map(int, input().split())

data = [[] for _ in range(n+1)]

for i in range(m):
    a,b=map(int, input().split())
    data[a].append(b)
    data[b].append(a)

#print(data)
distance = [False]*(n+1)

def bfs(x):
    que = deque([x])
    distance[x] = True
    while que:
        x= que.popleft()
        for i in data[x]:
            if not distance[i]:
                distance[i] = True
                que.append(i)

cnt = 0
for i in range(1, n+1):
    if not distance[i]:
        cnt +=1
        bfs(i)

print(cnt)
