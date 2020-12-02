import sys
sys.stdin = open("baekjoon_#9663_N퀸.txt", "r")

N = int(input())


def track(x,y, depth) :
    if depth == N :
        count += 1
        return

    else :
        for i in range(N) :
            if Mat[x][y] == 0 :
                Mat[x][i] = 1
                Mat[i][y] = 1
        k = x + y
        x=0
        while x >=0 and x<= N-1 and Mat[x][k-x] == 0 :
            Mat[x][k-x] = 1
            x += 1

Mat = [[0 for _ in range(N)] for _ in range(N)]