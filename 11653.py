a = int(input())
re = 0
while True:
    for i in range(2, a+1):
        if a % i == 0:
            print(i)
            a= a//i
            break
    if a == 1:
        break
