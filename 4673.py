def res():
    num=[]
    num2=[]
    for i in range(1,10001):
        num.append(i)
        if len(str(i)) == 1:
            a=i+int(str(i)[0])
        elif len(str(i)) ==2:
            a=i+int(str(i)[1])+int(str(i)[0])
        elif len(str(i)) ==3:
            a=i+int(str(i)[2])+int(str(i)[1])+int(str(i)[0])
        elif len(str(i)) == 4:
            a=i+int(str(i)[3])+int(str(i)[2])+int(str(i)[1])+int(str(i)[0])
        num2.append(a)

    for i in range(len(num2)):
        if num2[i] in num:
            num.remove(num2[i])

    for i in num:
        print(i)
res()
