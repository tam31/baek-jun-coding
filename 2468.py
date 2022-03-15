import sys
from collections import deque
sys.setrecursionlimit(100000)

dx=[-1,0,1,0]
dy=[0,1,0,-1]


#DFS
def dfs(num,x,y):
    temp[x][y] = 1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx>=0 and nx<n and ny>=0 and ny<n:
            if graph[nx][ny] > num and temp[nx][ny] == 0:
                temp[nx][ny] = 1
                dfs(num,nx,ny)
#BFS
def bfs(num,x,y):
    temp[x][y] = 1
    que = deque()
    que.append((x,y))
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx>=0 and nx <n and ny>=0 and ny<n:
                if graph[nx][ny] > num and temp[nx][ny] == 0:
                    que.append((nx,ny))
                    temp[nx][ny] = 1



n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
graph_min = min(map(min, graph))
graph_max = max(map(max, graph))


cnt_re = 0
for num in range(graph_max+1):
    cnt = 0
    temp =[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] > num and temp[i][j] == 0:
                bfs(num,i,j)
                cnt +=1
    cnt_re = max(cnt, cnt_re)
print(cnt_re)
