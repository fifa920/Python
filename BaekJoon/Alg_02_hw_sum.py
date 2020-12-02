import sys
sys.stdin = open("Alg_02_hw_sum.txt","r")


for t in range(10) :
    Num = int(input()) # 1번 받음
    arr = []
    for i in range(100) :
        arr.append(list(map(int,input().split())))  #arr 안에 list 형태로 100줄 불러옴

    max_row , max_col, max_R, max_L = 0, 0, 0, 0

    for a in range(100) :       # 오른쪽 대각선 합
        max_R += arr[a][a]

    for b in range(100) :       # 왼쪽 대각선 합
        max_L += arr[b][99-b]


    for c in range(100) :       # 각 행들의 합 중 최대 값
       max_1 = 0
       for d in range(100) :
           max_1 += arr[c][d]
           if max_1 > max_row :
               max_row = max_1

    for e in range(100) :       # 각 열들의 합 중 최대 값
        max_2 = 0
        for f in range(100) :
            max_2 += arr[f][e]
            if max_2 > max_col :
                max_col = max_2

    print('#{} {}'.format(Num, max(max_L, max_R, max_col, max_row)))