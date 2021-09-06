N,M = map(int, input().split())
pan = [list(map(int, input())) for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
visited = [[0]*M for _ in range(N)]

res = 1
q = [(0,0)]
visited[0][0] = 1

while q:
    y,x = q.pop(0)

    if y == N-1 and x == M-1:
        # print(y,x)
        break

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= nx < M and 0 <= ny < N and pan[ny][nx] == 1 and visited[ny][nx] == 0:
            q.append((ny,nx))
            visited[ny][nx] = visited[y][x] + 1

print(visited[N-1][M-1])