from collections import deque

N = int(input())
t1, t2 = map(int, input().split())
M = int(input())
arr = [[] for _ in range(N+1)]
for i in range(M):
    x,y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

visited = [0]*(N+1)
def bfs(start, target):
    q = deque([start])
    visited[start] = 1

    while q:
        node = q.popleft()
        for x in arr[node]:
            if visited[x] == 0:
                q.append(x)
                visited[x] = visited[node]+1

bfs(t1,t2)
if visited[t2]==0:
    print(-1)
else:
    print(visited[t2]-1)