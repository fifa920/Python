from collections import deque

N,K = map(int, input().split())
q = deque()
dist = [0]*100001


def bfs(N,K):
    q.append(N)

    while q:
        x = q.popleft()
        if x == K:
            return dist[x]
        else:
            for nx in [x-1, x+1, 2*x]:
                if 0<= nx <= 100000 and dist[nx] == 0:
                    q.append(nx)
                    dist[nx] = dist[x] + 1

print(bfs(N,K))