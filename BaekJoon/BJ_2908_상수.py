x,y = input().split()
new_x, new_y = 0, 0

for i in range(3):
    new_x += int(x[i])*10**(i)
    new_y += int(y[i])*10**(i)

print(max(new_x,new_y))