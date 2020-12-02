import sys
sys.stdin = open("Alg_swea_#5201_Advanced_컨테이너 운반.txt", "r")

T = int(input())

for t in range(1,T+1):
    N, M = map(int, input().split())
    N_list = list(map(int, input().split()))
    M_list = list(map(int, input().split()))

    N_list.sort(reverse=True)
    M_list.sort(reverse=True)
    x=0
    result = 0
    for i in range(len(N_list)):
        for j in range(x,len(M_list),1):
            if N_list[i] <= M_list[j] :
                result += N_list[i]
                x=j+1
                break

    print('#{} {}'.format(t,result))
