import sys
sys.stdin = open("BJ_7576_토마토.txt", "r")
from collections import deque

M, N = map(int, sys.stdin.readline().split())
pan = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
queue = deque()
ripe_list = []

def bfs(y, x):
    queue.append((y, x))
    while queue:

        y, x = queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue
            if pan[ny][nx] == -1:
                continue
            if pan[ny][nx] == 0:
                queue.append((ny, nx))
                pan[ny][nx] = pan[y][x] + 1

    for x in pan:
        if 0 in x:
            return -1
    return max(map(max, pan))-1


for y in range(N):
    for x in range(M):
        if pan[y][x] == 1:
            ripe_list.append((y,x))
for y,x in ripe_list:
    print(bfs(y,x))



# flag = True
#
# for y in range(N):
#     for x in range(M):
#         if pan[y][x] == 0:
#             flag = False
#
# if flag == False:
#     print(-1)
# else:
#     print(max(map(max, pan))-1)

# if flag == False:
#     print(-1)
# elif



