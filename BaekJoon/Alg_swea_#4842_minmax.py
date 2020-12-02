import sys
sys.stdin = open("Alg_swea_#4842_minmax.txt", "r")

T = int(input())

for t in range(1,T+1) :
    N = int(input())
    numbers_list = list(map(int, input().split()))
    temp_max = 0
    temp_min = 999999999999

    for i in range(N) :
        if numbers_list[i] > temp_max :
            temp_max = numbers_list[i]
        if numbers_list[i] < temp_min :
            temp_min = numbers_list[i]

    print(f'#{t} {temp_max - temp_min}')
