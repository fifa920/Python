import sys
sys.stdin = open('BJ_1012_유기농배추.txt', 'r')

def DFS(y, x):
    visited[y][x] = 1
    cnt = 0
    stack.append((y,x))

    while stack :
        (y,x) = stack.pop()

        for i in range(4):
            new_y = y + dy[i]
            new_x = x + dx[i]

            if 0 <= new_y < N and 0 <= new_x < M and visited[new_y][new_x] == 0 and pan[new_y][new_x] == 1 :
                stack.append((new_y, new_x))
                visited[new_y][new_x] = 1
    cnt += 1
    return cnt

for _ in range(T):
    M, N, K = map(int, input().split())
    pan = [[0]*M for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    res = 0
    stack = []

    for i in range(K):
        x,y = map(int, input().split())
        pan[y][x] = 1

    for y in range(N):
        for x in range(M):
            if pan[y][x] == 1 and visited[y][x] == 0 :
                res += DFS(y,x)
    print(res)

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 또 다른 방법
from collections import deque
T = int(input())

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def BFS(y,x):
    queue = deque()
    queue.append((y,x))
    visited[y][x] = 1
    cnt = 0

    while queue:
        (y,x) = queue.popleft()
        for i in range(4):
            new_y = y + dy[i]
            new_x = x + dx[i]
            if 0<= new_x < M and 0<= new_y < N and visited[new_y][new_x] ==0 and pan[new_y][new_x] == 1:
                queue.append((new_y,new_x))
                visited[new_y][new_x] = 1
    cnt += 1
    return cnt



for t in range(T):
    M, N, K = map(int, input().split())
    pan = [[0]*(M) for _ in range(N)]
    for _ in range(K):
        x,y = map(int, input().split())
        pan[y][x] = 1
    visited = [[0]*M for _ in range(N)]
    result = 0

    for y in range(N):
        for x in range(M):
            if pan[y][x] == 1 and visited[y][x] == 0 :
                result +=BFS(y,x)
    print(result)