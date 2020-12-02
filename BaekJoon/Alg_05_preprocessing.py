import sys
sys.stdin = open("Alg_05_preprocessing.txt", "r")



def DFS(here) :
    print(here)
    visited[here] = True

    for next in range(0, howmany) :
        if not visited[next] and Mymap[here][next] :
            DFS(next)


Data = list(map(int, input().split()))
howmany = len(Data) >> 1
Mymap = [[0]*(howmany+1) for i in range(howmany+1)]
visited = [0] * (howmany + 1)

for i in range(howmany) :
    Start = Data[2*i]
    Stop = Data[2*i+1]
    Mymap[Start][Stop] = 1
    Mymap[Stop][Start] = 1