import sys
sys.stdin = open("Alg_swea_#4834_숫자카.txt", "r")

T = int(input())
for t in range(1,T+1) :
    N = int(input())
    card_list = list(map(int, input()))
    result_list = [0] * 10

    for i in card_list :
        result_list[i] += 1
    temp = 0

    for i in range(9,-1, -1) :
        if result_list[i] > temp :
            temp = result_list[i]
            idx = i
    print(f'#{t} {idx} {result_list[idx]}')