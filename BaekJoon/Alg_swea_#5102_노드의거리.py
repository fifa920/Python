import sys
sys.stdin = open("Alg_swea_#5102_노드의거리.txt","r")

def bfs(start,end):
    Q.append(start)
    depth=1

    while Q :
        # print(Q)
        size = len(Q)
        for i in range(size):
            node = Q.pop(0)
            visited[node] = depth
            for x in range(1, V+1):
                if maze[node][x] == 1 and visited[x] == 0 and check[x] ==0 :
                    Q.append(x)
                    check[x] = 1

            # print(visited)
        depth+=1
    if visited[end] == 0 :
        return 0
    else :
        return visited[end] - 1

T = int(input())

for t in range(1,T+1) :
    V,E = map(int, input().split())
    maze = [[0]*(V+1) for _ in range(V+1)]
    for i in range(E):
        a,b = map(int, input().split())
        maze[a][b], maze[b][a] = 1, 1
    start, end = map(int, input().split())
    Q = []
    check = [0]*(V+1)
    visited = [0]*(V+1)
    # bfs(start,end)
    print('#{} {}'.format(t,bfs(start,end)))