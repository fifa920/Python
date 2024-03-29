# N = int(input())
# pan = []
#
# for i in range(N):
#     pan.append(list(map(int, input())))
#
# visited = [[0] * N for _ in range(N)]
#
# danji_cnt = 0
#
# dy = [-1, 0, 1, 0]
# dx = [0, 1, 0, -1]
#
# q = []
#
#
# def bfs(pan, y, x):
#     house_cnt = 1
#     visited[y][x] = 1
#     q.append((y, x))
#
#     while q:
#         y, x = q.pop(0)
#         for i in range(4):
#             ny = y + dy[i]
#             nx = x + dx[i]
#             if 0 <= ny < N and 0 <= nx < N and pan[ny][nx] == 1 and visited[ny][nx] == 0:
#                 visited[ny][nx] = 1
#                 q.append((ny, nx))
#                 house_cnt += 1
#
#     return house_cnt
#
#
# cnt = []
# for y in range(N):
#     for x in range(N):
#         if pan[y][x] == 1 and visited[y][x] == 0:
#             cnt.append(bfs(pan, y, x))
#
# print(len(cnt))
# cnt.sort()
# for x in cnt:
#     print(x)
from collections import deque
N = int(input())
pan = [list(map(int, input())) for _ in range(N)]

visited = [[0]*N for _ in range(N)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
q = deque()
house_lst = []

def bfs(pan,y,x):
    house_cnt = 1
    q.append((y,x))
    visited[y][x] = 1

    while q:
        by,bx = q.popleft()
        for i in range(4):
            ny = by + dy[i]
            nx = bx + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if pan[ny][nx] == 1 and visited[ny][nx] == 0:
                    q.append((ny,nx))
                    visited[ny][nx] = 1
                    house_cnt += 1
    house_lst.append(house_cnt)


for y in range(N):
    for x in range(N):
        if pan[y][x] == 1 and visited[y][x] == 0:
            bfs(pan,y,x)

print(len(house_lst))
house_lst.sort()
for i in range(len(house_lst)):
    print(house_lst[i])