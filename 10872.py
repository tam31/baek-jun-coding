def DFS(num):
    if num == 0:
        return 1
    else:
        return num*DFS(num-1)

a=int(input())
print(DFS(a))
