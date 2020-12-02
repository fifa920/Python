import sys
sys.stdin = open("Alg_swea_#1221_GNS.txt", "r")
T = int(input())

newdict = { 0:'ZRO' , 1:'ONE', 2:'TWO', 3:'THR', 4:'FOR', 5:'FIV', 6:'SIX', 7:'SVN', 8:'EGT', 9:'NIN'}


for t in range(1,T+1) :
    listed_data = []
    tc, N = map(str, input().split())
    str_list = list(map(str, input().split()))

    for i in range(10) :
        for j in range(int(N)) :
            if newdict[i] == str_list[j] :
                listed_data.append(newdict[i])

    print(f'#{t}')
    print(*listed_data)
