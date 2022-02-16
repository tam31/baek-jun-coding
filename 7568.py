n = int(input())
graph=[]
for i in range(n):
    graph.append(list(map(int, input().split())))

re=[]
for i in range(n):
    cnt = 1
    for j in range(n):
        if graph[i][0]<graph[j][0]:
            if graph[i][1] < graph[j][1]:
                cnt +=1
    re.append(cnt)
    print(re[i], end=' ')


