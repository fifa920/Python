import sys
sys.stdin = open("pascal.txt", "r")

T = int(input())

for t in range(1,T+1) :
    print(f'#{t}')
    N = int(input())
    lst = []
    for i in range(1, N+1) :
        lst.append(list([1]* i))

    for i in range(2, N):
        for j in range(1,i) :
            lst[i][j] = lst[i-1][j] + lst[i-1][j-1]

    for x in lst:
        print(*x)       # x 를 1차원 배열로 받고 *unpack을 이용해서 요소 하나씩 꺼냄.

    #print(f'{lst}')