from collections import deque


def bfs(m):
    data =[[] for _ in range(m+1)]

    data1 = list(map(int, input().split()))
    for i in range(1, m+1):
        data[i].append(data1[i-1])

    #print(data)

    graph = [False] * (m+1) #중복 반복을 막기위해
    x = 1#첫번쨰 시작
    cnt = 0 #결과값

    for x in range(1, m+1):
        if not graph[x]: 
            graph[x] = True    
            que = deque([x])
            while que:
                x= que.popleft()
                for i in data[x]:
                    if graph[i] == False:
                        graph[i] = True
                        que.append(i)
                        #print("i의 값", i)
                    else:
                        cnt += 1
                        #print("문제 i의값", i)
                        #print("cnt의 값", cnt)
    return cnt



n = int(input())
for i in range(n):
    m= int(input())
    print(bfs(m))
    
