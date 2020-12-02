import sys
sys.stdin = open("baekjoon_#1018_체스판.txt", "r")

N, M = map(int, input().split())
pan = [list(map(str, input())) for _ in range(N)]
cnt_list = []
standard_B = [0] * 8
standard_W = [0] * 8

for i in range(8) :
    if i % 2==0 :
        standard_B[i] = ['B','W','B','W','B','W','B','W']
        standard_W[i] = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']

    else :
        standard_B[i] = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
        standard_W[i] = ['B','W','B','W','B','W','B','W']

for x in range(M-7) :
    for y in range(N-7) :
        count_W = 0
        count_B = 0
        for i in range(8) :
            for j in range(8) :
                if pan[y+i][x+j] != standard_W[i][j] :
                    count_W += 1

                if pan[y+i][x+j] != standard_B[i][j] :
                    count_B += 1
        cnt_list.append(count_W)
        cnt_list.append(count_B)

print(min(cnt_list))