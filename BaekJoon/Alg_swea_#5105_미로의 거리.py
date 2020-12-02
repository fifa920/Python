import sys
sys.stdin = open("Alg_swea_#5105_미로의 거리.txt","r")

def BFS(y,x):
    global result
    queue.append((y,x))

    #큐가 비어있지 않으면
    while queue :
        (y,x) = queue.pop(0)

        for i in range(4):
            newX = x+dx[i]
            newY = y+dy[i]

            if 0<=newX<N and 0<= newY < N and (maze[newY][newX] ==0 or maze[newY][newX] ==3) and visited[newY][newX]==0:
                queue.append((newY,newX))
                visited[newY][newX] = visited[y][x]+1

                if maze[newY][newX] == 3:
                    result = visited[newY][newX]-1
                    return
T = int(input())

for t in range(1,T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    queue = []
    result = 0

    for i in range(N) :
        for j in range(N):
            if maze[i][j] == 2 :
                x = j
                y = i
    BFS(y,x)
    print('#{} {}'.format(t,result))