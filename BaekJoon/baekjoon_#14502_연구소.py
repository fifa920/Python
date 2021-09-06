from collections import deque
import sys
N,M = map(int, sys.stdin.readline().split())
pan = []

q = deque()
max_result = 0

for i in range(N):
    pan.append(list(map(int, sys.stdin.readline().split())))

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs():
    global max_result

    copy_pan = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            copy_pan[i][j] = pan[i][j]

    result = 0
    for y in range(N):
        for x in range(M):
            if pan[y][x] == 2:
                q.append((y,x))
    while q:
        y,x = q.popleft()
        for j in range(4):
            ny = y + dy[j]
            nx = x + dx[j]
            if 0 <= ny < N and 0 <= nx < M and copy_pan[ny][nx] == 0:
                copy_pan[ny][nx] = 2
                q.append((ny,nx))
    for k in copy_pan:
        for l in k:
            if l == 0:
                result += 1
    max_result = max(result, max_result)




def wall(wall_cnt):
    if wall_cnt == 3:
        bfs()
        return

    else:
        for y in range(N):
            for x in range(M):
                if pan[y][x] == 0:
                    pan[y][x] = 1
                    wall(wall_cnt+1)
                    pan[y][x] = 0

wall(0)
print(max_result)
