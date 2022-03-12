#내가 푼방식
n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

data=[]
cnt = 1
def dfs(num,x,y):
    global cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx>=0 and nx<n and ny>=0 and ny<n:
            if graph[nx][ny] == 1:
                cnt +=1
                graph[nx][ny] = num
                dfs(num, nx, ny)


num = 2
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            graph[i][j] = num
            dfs(num,i,j)
            data.append(cnt)
            cnt = 1
            num +=1
data.sort()
print(num-2)
#print(graph)
for i in range(len(data)):
    print(data[i])

