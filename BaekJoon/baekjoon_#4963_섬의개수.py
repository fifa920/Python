import sys
from collections import deque

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

def bfs(y,x):
    global q, cnt
    q.append((y,x))
    visited[y][x] = 1

    while q:
        (ay,ax) = q.popleft()
        for i in range(8):
            ny = ay + dy[i]
            nx = ax + dx[i]
            if 0 <= ny < h and 0 <= nx < w and visited[ny][nx] == 0 and pan[ny][nx] == 1:
                q.append((ny,nx))
                visited[ny][nx] = 1

    cnt += 1


while True:
    w,h = map(int, sys.stdin.readline().split())
    if (w,h) == (0,0):
        break
    else:
        pan = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
        visited = [[0]*w for _ in range(h)]
        q = deque()
        cnt = 0

        for y in range(h):
            for x in range(w):
                if pan[y][x] == 1 and visited[y][x] == 0:
                    bfs(y,x)
        print(cnt)



