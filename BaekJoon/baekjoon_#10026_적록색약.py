from collections import deque

N = int(input())
arr = [list(input()) for _ in range(N)]

# G = R 로 보는게 적록색약

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
visited = [[0]*N for _ in range(N)]

def bfs(y,x, arr):
    # q = deque((y,x))
    q = deque()
    q.append((y,x))
    visited[y][x] = 1
    while q:
        y,x = q.popleft()
        # print(y,x)

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if arr[ny][nx] == arr[y][x] and visited[ny][nx] == 0:
                    q.append((ny,nx))
                    visited[ny][nx] = 1
result = 0
for y in range(N):
    for x in range(N):
        if visited[y][x] == 0:
            bfs(y,x,arr)
            result += 1
# print(result)

for y in range(N):
    for x in range(N):
        if arr[y][x] == 'R':
            arr[y][x] = 'G'
res = 0
visited = [[0]*N for _ in range(N)]
for y in range(N):
    for x in range(N):
        if visited[y][x] == 0:
            bfs(y,x,arr)
            res += 1
print(result, res)