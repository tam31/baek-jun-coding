from collections import deque

n,k = map(int, input().split())
graph = []
data = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))

data.sort()
q = deque(data)

t_s,t_x,t_y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while q:
    virus, s, x, y = q.popleft()
    if s == t_s:
        break
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx >=0 and nx <n and ny >=0 and ny <n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus,s+1,nx,ny))
print(graph[t_x-1][t_y-1])

'''
n, k = map(int, input().split())

data = []
for i in range(n):
    data.append(list(map(int, input().split())))

temp=[[0]*n for _ in range(n)]
#print(temp)
for i in range(n):
    for j in range(n):
        temp[i][j] = data[i][j]

dx = [-1,0,1,0]
dy = [0,1,0,-1]


def dfs(number):
    
    num = number
    for i in range(n):
        for j in range(n):
            if data[i][j] == num:
                #print(i, j)
                for z in range(4):
                   # print("z:%d" %z)
                    nx = i + dx[z]
                    ny = j + dy[z]
                    if nx >=0 and nx <n and ny >=0 and ny <n:
                        if data[nx][ny] == 0:
                            temp[nx][ny] = num
                          #  print("바뀐값[nx] %d [ny] %d:" %(nx, ny))
    for i in range(n):
        for j in range(n):
            data[i][j] = temp[i][j]

s,mx,my = map(int, input().split())
for i in range(s):
   # print()
   # print("s번째: %d" %i)
    for j in range(1, k+1):
        dfs(j)
print(data[mx-1][my-1])
'''
