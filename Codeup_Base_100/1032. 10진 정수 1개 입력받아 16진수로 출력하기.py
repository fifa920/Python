x=int(input())
y=hex(x)
list_y=[]
for i in str(y):
    list_y.append(i)

for a in range(2,len(list_y)):
    print(list_y[a], end='')