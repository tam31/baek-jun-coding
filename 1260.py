import sys
from collections import deque

n, m, x = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
#print(graph)

for i in range(n+1):
    graph[i].sort()

data = [-1]*(n+1)

def dfs(x):
    print(x, end=' ')
    data[x] = 0
    for i in graph[x]:
        if data[i] == -1:
            dfs(i)

def bfs(x):
    
    data[x] = 0
    que = deque([x])
    while que:
        x = que.popleft()
        
        print(x, end=' ')
        
        graph[x].sort()
        for i in graph[x]:
            if data[i] == -1:
                data[i] = data[x] + 1
                que.append(i)




dfs(x)
data = [-1]*(n+1)
print()
bfs(x)
