num = int(input())
re = 0
t=True
for i in range(0, num//3+1):
    for j in range(0, num//5+1):
        if i*3+j*5==num:
            re = (i+j)
            t=False
            break
        else:
            re = -1
        
    if t == False:
        break

print(re)

suger = int(input())
bag = 0
while suger >=0:
    if suger %5 == 0:
        bag += suger//5
        print(bag)
        break
    suger -=3
    bag +=1
else:
    print(-1)
