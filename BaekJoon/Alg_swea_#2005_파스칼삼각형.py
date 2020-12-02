import sys
sys.stdin = open("Alg_swea_#2005_파스칼삼각형.txt", "r")

T = int(input())

for t in range(1,T+1) :
    N = int(input())
    lst = []

    if N == 1 :
        lst = [1]
    elif N == 2 :
        lst = [[1], [1, 1]]
    elif N>=3 :
        lst = [[1], [1, 1]]
        lst = [[1] for _ in range(2,N)]
        for i in range(2, N):
            for j in range(0,i-1):
                lst[i].extend(lst[i - 1][j] + lst[i - 1][j+1])
        print(lst)












