import sys
sys.stdin = open("Alg_swea_#4835_구간합.txt", "r")

T = int(input())

for t in range(1,T+1) :
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    temp_list = []

    for i in range(N-M+1) :
        total = 0
        for j in range(M):
            total += numbers[i+j]
        temp_list.append(total)

    print(f'#{t} {max(temp_list) - min(temp_list)}')