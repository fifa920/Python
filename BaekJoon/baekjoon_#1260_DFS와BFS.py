import sys
sys.stdin = open("baekjoon_#1260_DFS와BFS.txt","r")

def DFS(start) :
    visitedd[start] = 1
    resultd.append(start)

    for i in range(1,V+1):
        if mat[start][i] == 1 and visitedd[i] == 0 :
            DFS(i)
    return resultd

def BFS(start):
    visitedb[start] = 1
    queue.append(start)

    for i in range(1,V+1):
        node = queue.pop(-1)
        if mat[node][i] == 1 and visitedb[i] == 0 :
            visitedb[i] = 1
            queue.append(i)





V,E,start = map(int, input().split())
mat = [[0]*(V+1) for _ in range(V+1)]
for i in range(E):
    a,b = map(int, input().split())
    mat[a][b], mat[b][a] = 1, 1
visitedd = [0] * (V + 1)
visitedb = [0] * (V + 1)
queue = []
resultd = []
resultb=[]

print(DFS(start))