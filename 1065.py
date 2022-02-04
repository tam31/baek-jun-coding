def res(a):
    count = 0
    for i in range (1, a+1):
        if i<100:
            count +=1
        else:
            if int(str(i)[0])-int(str(i)[1]) == int(str(i)[1])-int(str(i)[2]):
                count +=1
    print(count)

a = int(input())
res(a)
