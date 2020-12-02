import sys
sys.stdin = open("graphpath.txt","r")

T = int(input())

for t in range(1,T+1) :
    V, E = map(int, input().split()) # 6 5
    list_path = [[0 for i in range(V+1)] for _ in range(V+1)]

    for i in range(E) :
        start, stop = map(int, input().split())
        list_path[start][stop] = 1

    first, end = map(int, input().split())
    visited = [0] * (V+1)
    visited[first] = 1

    for a in range(first,V+1) :
        for b in range(1, V+1) :
            if list_path[a][b] == 1 and visited[a] != 1 :

