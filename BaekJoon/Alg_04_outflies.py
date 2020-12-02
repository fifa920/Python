import sys
sys.stdin = open("Alg_04_outflies.txt", "r")

T = int(input())

for t in range(1,T+1) :
    N,M = map(int, input().split())
    fly_list = [list (map(int, input().split())) for i in range(N)]

    list_sum = []

    for k in range(0,N-M+1) :
        for w in range(0,N-M+1) :
            m_sum = 0
            for i in range(0, M):
                for j in range(0, M):
                    m_sum += fly_list[i + w][j + k]
            list_sum.append(m_sum)

    print('#{0} {1}'.format(t, max(list_sum)))

