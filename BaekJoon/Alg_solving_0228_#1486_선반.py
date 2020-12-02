import sys
sys.stdin = open("Alg_solving_0228_#1486_선반.txt", "r")

T = int(input())
for t in range(1,T+1) :
    N,B = map(int,input().split())
    height_list = list(map(int, input().split()))
    n = len(height_list)
    sum_height = sum(height_list)
    temp=[]

    if N == 1 and sum_height >= B :
        print('#{} {}'.format(t, sum_height - B))
    else :
        for i in range(1<<n) :
            y = 0
            for j in range(n) :
                x = i & (1<<j)
                if x :
                    y += height_list[j]
                    if y >= B :
                        temp.append(y)
        print('#{} {}'.format(t, min(temp)-B))


