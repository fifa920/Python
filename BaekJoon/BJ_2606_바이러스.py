import sys
sys.stdin = open("BJ_2606_바이러스.txt", "r")

from collections import deque
queue = deque()

Computers = int(input())
Connects = int(input())

pan=[[0]*(Computers+1) for _ in range(Computers+1)]

for i in range(Connects):
    x,y = map(int, input().split())
    pan[x][y] = pan[y][x] = 1

visited = [0]*(Computers+1)

def bfs(start):
    queue.append(start)
    visited[start] = 1
    while queue :
        x = queue.popleft()
        for i in range(1,Computers+1):
            if pan[x][i] == 1 and visited[i] == 0 :
                queue.append(i)
                visited[i] = 1
    print(sum(visited)-1)


bfs(1)