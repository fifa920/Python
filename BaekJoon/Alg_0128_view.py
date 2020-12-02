import sys
sys.stdin = open("view.txt","r")

T = 10

for t in range(1,T+1) :
    N = int(input())
    floor_list = list(map(int, input().split()))
    total = 0


    for i in range(2,N-2) :
        maxH = 0
        for j in [-2, -1, 1, 2] :
            if maxH < floor_list[j+i] :
                maxH = floor_list[i+j]
            diff = floor_list[i] - maxH
            if diff >0 :
                total += diff

    print(total)