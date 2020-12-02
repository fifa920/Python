import sys
sys.stdin = open("Alg_Solving_0206_#1267_작업순.txt", "r")

def DFS(here) :
    print(here)
    visited[here] = 1

    for next in range(V) :
        if Mymap[here][next] == 1 and not visited[next] :
            DFS(next)

T = 10

for t in range(1,T+1) :
        V, E = map(int, input().split())
        edge_list = list(map(int, input().split()))
        Mymap = [[0 for _ in range(V + 1)] for _ in range(V + 1)]
        visited = [0] * (V + 1)

        for i in range(E) :
            start = edge_list[2*i]
            end = edge_list[2*i + 1]
            Mymap[start][end] = 1



        DFS(edge_list[0])

