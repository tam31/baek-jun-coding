a=input()
b=''
for i in range(len(a)):
    b += a[len(a)-i-1]
if a == b:
    print(1)
else:
    print(0)
