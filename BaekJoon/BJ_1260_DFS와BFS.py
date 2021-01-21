from collections import deque
import sys
sys.stdin = open("BJ_1260_DFS와BFS.txt", "r")

V,E,start = map(int, input().split())

pan = [[0]*(V+1) for _ in range(V+1)]
for _ in range(E):
    y,x = map(int, input().split())
    pan[y][x], pan[x][y] = 1,1

visited = [0] * (V + 1)
stack = []
queue = deque()

def dfs(start):

    visited[start] = 1
    print(start, end=' ')
    for i in range(1,V+1):
        if visited[i] == 0 and pan[start][i] == 1 :
            dfs(i)


def bfs(start):
    vis = [0] * (V + 1)
    queue.append(start)
    vis[start] = 1
    while queue :
        x = queue.popleft()
        print(x, end=' ')
        for i in range(1,V+1):
            if vis[i] == 0 and pan[x][i] == 1 :
                queue.append(i)
                vis[i] = 1
dfs(start)
print()
bfs(start)

