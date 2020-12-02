import sys
sys.stdin = open("Alg_mocktest.txt","r")

def find(y,x,M):
    global count
    for k in range(8):
        newX, newY = x+dx[k], y+dy[k]
        if 0<=newX<10 and 0<=newY<10 and M[newY][newX] == 1 and visited[newY][newX] == 0 :
            visited[newY][newX] = 1
            find(newY, newX, M)

T = int(input())

for t in range(1,T+1):
    M = [list(map(int, input().split())) for _ in range(10)]
    visited = [[0]*10 for _ in range(10)]
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    count = 0
    for y in range(10):
        for x in range(10):
            if M[y][x] == 1 and visited[y][x] == 0 :
                find(y,x,M)
                count+=1

    print('#{} {}'.format(t, count))





