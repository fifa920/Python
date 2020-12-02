import sys
sys.stdin = open("List1_sum_hw4.txt","r")

T = int(input())

for i in range(1,T+1) :

    N, M = map(int,input().split())
    num_list = list(map(int, input().split()))

    hap_list = []

    for j in range(0, N-M+1) :
        result = 0
        for k in range(0, M) :
            result = result + num_list[k+j]

        hap_list.append(result)

    diff = max(hap_list) - min(hap_list)
    print('#{0} {1}'.format(i,diff))

