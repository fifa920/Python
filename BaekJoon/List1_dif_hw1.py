import sys
sys.stdin = open("List1_dif_hw1.txt","r")

T = int(input())

for i in range(1,T+1) : # i = 1 2 3
    N = int(input())
    numbers = list(map(int, input().split()))

    for j in range(N-1,0,-1) :
        for k in range(0,N-1) :
            if numbers[k] >= numbers[k+1] :
                numbers[k], numbers[k+1] = numbers[k+1], numbers[k]

    result = numbers[N-1] - numbers[0]
    print('#{0} {1}'.format(i, result))


