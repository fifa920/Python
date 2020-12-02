import sys
sys.stdin = open("Alg_swea_#4836_색칠하.txt", "r")

T = int(input())

for t in range(1,T+1) :
    N = int(input())
    color_list = [list(map(int, input().split())) for _ in range(N)]
    pan = [list(0 for _ in range(10)) for _ in range(10)]


    for i in range(N) :
        x1 ,y1 = color_list[i][0], color_list[i][1]
        x2, y2 = color_list[i][2], color_list[i][3]

        for j in range(x1, x2+1):
            for k in range(y1, y2+1):
                pan[j][k] += color_list[i][4]

    count = 0
    for a in range(10) :
        for b in range(10) :
            if pan[a][b] == 3 :
                count += 1

    print(f'#{t} {count}')


