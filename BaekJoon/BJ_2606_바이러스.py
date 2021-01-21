from collections import deque
import sys
sys.stdin = open("BJ_2606_바이러스.txt", "r")

N = int(input())
E = int(input())
pan = [[0]*(N+1) for _ in range(N+1)]
for _ in range(E):
    y,x = map(int, input().split())
    pan[y][x] = pan[x][y] = 1

visited=[0]*(N+1)


def BFS(v):
    cnt = 0
    queue = deque([v])
    visited[v] = 1
    while queue:
        node = queue.popleft()
        for i in range(1,N+1):
            if pan[node][i] == 1 and visited[i] == 0:
                queue.append(i)
                cnt += 1
                visited[i] = 1
    return cnt
print(BFS(1))

# from collections import deque
# queue = deque()
#
# Computers = int(input())
# Connects = int(input())
#
# pan=[[0]*(Computers+1) for _ in range(Computers+1)]
#
# for i in range(Connects):
#     x,y = map(int, input().split())
#     pan[x][y] = pan[y][x] = 1
#
# visited = [0]*(Computers+1)
#
# def bfs(start):
#     queue.append(start)
#     visited[start] = 1
#     while queue :
#         x = queue.popleft()
#         for i in range(1,Computers+1):
#             if pan[x][i] == 1 and visited[i] == 0 :
#                 queue.append(i)
#                 visited[i] = 1
#     print(sum(visited)-1)
#
#
# bfs(1)