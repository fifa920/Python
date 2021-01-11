import sys
sys.stdin = open("Alg_swea_#4835_구간합.txt", "r")

T = int(input())

# for t in range(1,T+1) :
#     N, M = map(int, input().split())
#     numbers = list(map(int, input().split()))
#
#     temp_list = []
#
#     for i in range(N-M+1) :
#         total = 0
#         for j in range(M):
#             total += numbers[i+j]
#         temp_list.append(total)
#
#     print(f'#{t} {max(temp_list) - min(temp_list)}')


for t in range(1,T+1) :
    N,M = map(int, input().split())
    arr = list(map(int, input().split()))
    S = 0
    for i in range(M):
        S += arr[i]
    Max = Min = S

    # 두 번째 구간합은 첫 번째 구간합에서 +arr[i] - arr[i-M]
    for i in range(M,N):
        S += (arr[i] - arr[i-M])

        Min = min(S, Min)
        Max = max(S, Max)

    result = Max - Min

    print("#{} {}".format(t, result))