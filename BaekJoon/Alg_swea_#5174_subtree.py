import sys
sys.stdin = open("Alg_swea_#5174_subtress.txt", "r")

def subtree(N):
    visited[N] == 1
    global count

    if pan[N][1] == 0 and pan[N][2] == 0 :
        return count
    else :
        for i in range(1,3):
            if pan[N][i] and visited[pan[N][i]] == 0 :
                visited[pan[N][i]] = 1
                count += 1
                next = pan[N][i]
                subtree(next)



T = int(input())

for t in range(1,T+1):
    E, N = map(int, input().split())
    pan = list([0]*(3) for _ in range(E+2))
    data = list(map(int, input().split()))
    visited=[0]*(E+2)
    count = 1
    for i in range(0,len(data),2):
        parent, child = data[i], data[i+1]
        if pan[parent][1] == 0 :
            pan[parent][1] = child
        else :
            pan[parent][2] = child
    subtree(N)
    print('#{} {}'.format(t,count))






# V = int(input())
# E = V-1
# arr = list(map(int, input().split()))
# L = [0]*(V+1)
# R = [0]*(V+1)
# P = [0]*(V+1)
#
# for i in range(0, len(arr),2):
#     parent, child = arr[i], arr[i+1]
#     if L[parent] :
#         R[parent]= child
#     else:
#         L[parent] = child
#     P[child] = parent
#
# def inorder(v) : # 방문하는 노드 번호
#     if v == 0 :
#         return
#     inorder(L[v])
#     inorder(R[v])