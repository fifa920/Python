import sys
sys.stdin = open("Alg_swea_#1208_Flatten(평탄화).txt", "r")

T = 10

for t in range(1,T+1) :
    N = int(input())         # 덤프하는 횟수
    lst = list(map(int, input().split()))
    count = 0               #덤프 하면 올리는 횟수

    while count != N :
        x = lst.index(max(lst))
        y = lst.index(min(lst))
        lst[x] -= 1
        lst[y] += 1
        count += 1
    print(f'#{t} {max(lst) - min(lst)}')