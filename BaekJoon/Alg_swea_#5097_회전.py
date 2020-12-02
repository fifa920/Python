import sys
sys.stdin = open("Alg_swea_#5097_회전.txt","r")

T = int(input())

for t in range(1,T+1):
    N,M = map(int, input().split())
    lst = list(map(int, input().split()))

    for i in range(M):
        lst.append(lst.pop(0))
    print('#{} {}'.format(t,lst[0]))