import sys
sys.stdin = open("Alg_swea_#2001_파리퇴치.txt","r")

def cal(x,y) :
    sum=0
    for i in range(x,x+M):
        for j in range(y,y+M):
            sum += pan[i][j]
    return sum

T = int(input())

for t in range(1,T+1):
    N,M = map(int, input().split())
    pan = [list(map(int, input().split())) for _ in range(N)]
    max_val = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            hap = cal(i,j)
            if hap > max_val:
                max_val = hap
    print(f'#{t} {max_val}')
