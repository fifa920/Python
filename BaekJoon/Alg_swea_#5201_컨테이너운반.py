import sys
sys.stdin = open('Alg_swea_#5201_Advanced_컨테이너 운반.txt', 'r')

T = int(input())

for tc in range(T):
    N,M = map(int, input().split())
    N_list = list(map(int, input().split()))
    M_list = list(map(int, input().split()))

    result = 0
    x = 0
    N_list.sort(reverse = True)
    M_list.sort(reverse = True)

    for i in N_list :
        for j in range(x,len(M_list)) :
            if M_list[j] >= i :
                result += i
                x+=1
                break
    print(f'#{tc+1} {result}')

