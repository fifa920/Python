import sys
sys.stdin = open("Alg_swea_#6190_단조증가.txt", "r")

T = int(input())

for t in range(1,T+1) :
    N = int(input())
    numbers = list(map(int, input().split()))
    result = []

    for i in range(N-1):
        for j in range(i+1,N):
            check = 0
            y = numbers[i]*numbers[j]
            x = str(numbers[i]*numbers[j])
            for k in range(len(x)-1) :
                if int(x[k]) <= int(x[k+1]) :
                    pass
                else :
                    check += 1
                    break
            if check == 0 :
                result.append(y)

    if len(result) != 0 :
        print(f'#{t} {max(result)}')
    else :
        print(f'#{t} -1')
