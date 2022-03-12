from collections import deque

n = int(input())
k = int(input())
data = [[] for _ in range(n+1)]
for i in range(k):
    a,b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)
print(data)
graph = [0]*(n+1)

def bfs(x):
    graph[x] = 1
    cnt = 0
    que = deque([x])
    
    while que:
        x = que.popleft()
        for i in data[x]:
            if graph[i] == 0:
                graph[i] = graph[x] +1
                que.append(i)
                cnt += 1
    return cnt

print(bfs(1))
