import sys
sys.stdin = open("Alg_swea_#1209_Sum.txt", "r")

T = 10

for t in range(1,T+1) :
    N = int(input())
    Mymap = [list(map(int, input().split())) for _ in range(100)]

    sum_RD = 0
    sum_LD = 0
    temp = []

    for y in range(100) :
        sum_ver = 0
        sum_hor = 0
        for x in range(100) :
            sum_ver += Mymap[y][x]
            sum_hor += Mymap[x][y]

        temp.append(sum_ver)
        temp.append(sum_hor)

    for x in range(100) :
        sum_LD += Mymap[x][99-x]
        sum_RD += Mymap[x][x]
    temp.append(sum_LD)
    temp.append(sum_RD)

    print(f'#{N} {max(temp)}')
