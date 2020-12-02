import sys
sys.stdin = open("Alg_solving_0226_버스노선.txt", "r")

T = int(input())
for t in range(1,T+1) :
    N = int(input())
    stop_list = [0] * 5001
    temp = [0] * 5001

    for i in range(1,N+1) :
        A_i, B_i = map(int, input().split())
        for j in range(A_i, B_i+1) :
            stop_list[j] += 1

    C = int(input())
    print('#{}'.format(t), end = ' ')

    for _ in range(C) :
        x = int(input())
        if _ != C-1 :
            print(stop_list[x], end=' ')
        else :
            print(stop_list[x])

