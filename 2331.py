#더 간단한 방법
a,p = map(int, input().split())
nums = [a]
while True:
    tmp = 0
    for s in str(nums[-1]):
        tmp += int(s)**p

    if tmp in nums:
        break

    nums.append(tmp)

print(nums.index(tmp))

'''
내가 푼 방식
a,p = input().split()
p = int(p)
data = []
data.append(int(a))
re2 = 1

def dfs(a,p):
    
    sum = 0
    for i in range (len(a)):
        sum += int(a[i])**p
    data.append(sum)
    #print(data)
    check()
    if re2 == 2:
        #print("마지막 ", data)
        return
    dfs(str(sum), p)
    
    
def check():
    global re2
    for i in range(len(data)):
        cnt = 0
        for j in range(i+1, len(data)):
            if data[i] == data[j]:
                cnt +=1
            if cnt == 2:
                re = data.index(data[i])
                del data[re:]
                re2 = 2
                return re2

dfs(a,p)
print(len(data))
'''
