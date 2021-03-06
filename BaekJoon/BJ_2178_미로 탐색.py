import sys
sys.stdin = open("BJ_2178_미로 탐색.txt", "r")
# from collections import deque
#
#
# N,M = map(int, input().split())
# pan = [list(map(int, input())) for _ in range(N)]
# dy = [-1, 0, 1, 0]
# dx = [0, 1, 0, -1]
#
#
# def bfs(y,x):
#     queue = deque()
#     queue.append((y,x))
#
#     while queue:
#         y,x = queue.popleft()
#         for i in range(4):
#             ny = y + dy[i]
#             nx = x + dx[i]
#
#             if nx < 0 or nx >= M or ny < 0 or ny >= N :
#                 continue
#             if pan[ny][nx] == 1 :
#                 pan[ny][nx] = pan[y][x] + 1
#                 queue.append((ny,nx))
#     return pan[N-1][M-1]
#
# print(bfs(0,0))

from _collections import deque
N,M = map(int, input().split())
pan = [list(map(int, input())) for _ in range(N)]

dy = [-1,0,1,-1]
dx = [0,1,0,-1]

def BFS(y,x):
    queue = deque()
    queue.append((y,x))

    while queue:
        (p_y, p_x) = queue.popleft()

        for i in range(4):
            n_y = p_y + dy[i]
            n_x = p_x + dx[i]

            if 0<= n_y <N and 0<= n_x < M and pan[n_y][n_x] == 1:
                queue.append((n_y,n_x))
                pan[n_y][n_x] = pan[p_y][p_x] + 1

BFS(0,0)
print(pan[N-1][M-1])








