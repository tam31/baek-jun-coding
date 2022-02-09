def re(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else :
        return re(num-2)+ re(num-1)
a=int(input())
print(re(a))
