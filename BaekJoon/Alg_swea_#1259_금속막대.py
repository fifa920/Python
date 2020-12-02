import sys
sys.stdin = open("Alg_swea_#1259_금속막대.txt", "r")

T = int(input())

def find(start, end) :
    sort_nasa.append([start,end])
    count = 0
    #for i in range(N) :
    while count != N-1 :
        for i in range(N):
            if nasa_list[i][1] == start :
                sort_nasa.insert(0, [nasa_list[i][0], nasa_list[i][1]])
                start = nasa_list[i][0]
                count += 1
            if nasa_list[i][0] == end :
                sort_nasa.append([nasa_list[i][0], nasa_list[i][1]])
                end = nasa_list[i][1]
                count += 1

    for i in range(N) :
        print(f'{sort_nasa[i][0]} {sort_nasa[i][1]}', end = ' ' )
    print()


for t in range(1, T+1) :

    N = int(input())
    lst = list(map(int, input().split()))
    nasa_list = []
    sort_nasa = []

    for i in range(0,2*N,2) :
        nasa_list.append([lst[i],lst[i+1]])

    print(f'#{t}', end = " ")
    find(lst[0],lst[1])

