import sys
sys.stdin = open("Alg_swea_#2805_농작물수확하기.txt", "r")

T = int(input())
for t in range(1,T+1):
    N = int(input())
    pan = [list(map(int, input())) for _ in range(N)]
    result = 0

    s = e = N//2
    for row in range(N):
        for x in range(s,e+1):
            result += pan[row][x]
        if row < N//2:
            s -=1
            e +=1
        else:
            s += 1
            e -= 1
    print("#{} {}".format(t,result))