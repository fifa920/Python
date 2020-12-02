import sys
sys.stdin = open("Alg_swea_#5188_Advanced_최소합.txt", "r")

def dfs(y, x):
    down = right = N * 11
    if y == x >= N - 1:
        return arr[y][x]
    else:
        if y < N - 1:
            down = dfs(y + 1, x)
        if x < N - 1:
            right = dfs(y, x + 1)
    if down >= right:
        return right + arr[y][x]
    else:
        return down + arr[y][x]


T = int(input())

for t in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N) ]
    print(dfs(0,0))

