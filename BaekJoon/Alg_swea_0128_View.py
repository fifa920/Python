import sys
sys.stdin = open("Alg_swea_0128_View.txt", "r")

T = 10

for t in range(1,T+1) :
    N = int(input())
    lst = list(map(int, input().split()))
    total = 0


    for i in range(2,N-2) :
        if lst[i] > lst[i-2] and lst[i] > lst[i-1] and lst[i] > lst[i+1] and lst[i] > lst[i+2] :
            temp = []
            for j in [-2, -1, 1, 2] :
                temp.append(lst[i]-lst[i+j])
            total += min(temp)
    print(total)
