import sys
sys.stdin = open("Alg_swea_#5110_수열 합치기.txt", "r")

def merge():
    lst = list(map(int, input().split()))

    for i in range(M-1):
        comList = list(map(int, input().split()))
        leng = len(lst)
        for x in lst :
            if comList[0] < x :
                idx = lst.index(x)
                lst[idx:idx] = comList
                break
        if len(lst) == leng :
            lst.extend(comList)

    return lst



T = int(input())

for t in range(1,T+1) :
    N, M = map(int,input().split())
    # lst_1 = list(map(int, input().split()))

    print('#{}'.format(t), end= ' ')
    print(*(merge()[-1:-11:-1]))

