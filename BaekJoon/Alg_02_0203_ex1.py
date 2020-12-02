import sys
sys.stdin = open('Alg_02_0203_ex1.txt','r')



def IsSafe(y,x) :
    if y>=0 and y<5 and x>=0 and x<5 : return True
    return False

def MyAbs(y,x) :
    if y> x : return y-x
    else : return x-y

Data = [0 for _ in range(5) for _ in range(5)]

for i in range(5) :
    Data[i] = list(map(int,input().split()))

dy = [-1, 1, 0, 0,]
dx = [0, 0, -1, 1]

sum = 0
for y in range(5) :
    for x in range(5) :
        for dir in range(4) :
            newY = y + dy[dir]
            newX = x + dx[dir]

            if IsSafe(newY, newX) :
                 sum += MyAbs(Data[y][x], Data[newY][newX])

print(sum)

