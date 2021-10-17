from collections import deque

N = int(input())

pan = [list(map(int, input().split())) for _ in range(N)]
max_number = max(max(pan))
ans = 1
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(h,visited, y,x):
    q = deque()
    q.append((y,x))
    visited[y][x] = 1
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N and pan[ny][nx] > h and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                q.append((ny,nx))



for h in range(1,max_number):
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for y in range(N):
        for x in range(N):
            if pan[y][x] > h and visited[y][x] == 0:
                bfs(h,visited,y,x)
                cnt += 1
    if ans < cnt:
        ans = cnt

print(ans)