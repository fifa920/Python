import sys
sys.stdin = open('Alg_swea_#5202_화물도크.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())
    time_list = [list(map(int, input().split())) for _ in range(N)]
    sorted_list = sorted(time_list, key = lambda x : (x[1], x[0]))
    end_time = sorted_list[0][1]
    result = 1

    for i in range(1,N):
        if sorted_list[i][0] >= end_time :
            result += 1
            end_time = sorted_list[i][1]
    print(f'#{tc+1} {result}')