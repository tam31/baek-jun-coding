list_x=[]
list_y=[]
for i in range(3):
        x,y = map(int, input().split())
        list_x.append(x)
        list_y.append(y)

for i in range(3):
        if list_x.count(list_x[i]) == 1:
                x2=list_x[i]        
        if list_y.count(list_y[i]) == 1:
                y2=list_y[i]
                
print(x2,y2)
