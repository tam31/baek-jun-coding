while (1):
        num = list(map(int, input().split()))
        if sum(num) == 0:
                break
        c= max(num)
        num.remove(c)
        if num[0] **2 + num[1]**2 == c**2:
                print('right')
        else:
                print('wrong')
        
