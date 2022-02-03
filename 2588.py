num1 = int(input())
num2 = int(input())

print(num1 * (num2%10))
print(num1 * ((num2%100)//10))
print(num1 * (num2//100))
print(num1 * num2)


'''
처음푼 방식
a=input()
b=input()
c=0
d=0
sum = 0
for i in range(0, 3):
    c = b[2-i]
    d = int(a)*int(c)
    print(d)
    sum +=d *(10**i)
print(sum)
'''
    
