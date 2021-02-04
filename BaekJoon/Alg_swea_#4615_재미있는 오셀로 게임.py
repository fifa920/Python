import sys
sys.stdin = open("Alg_swea_#4615_재미있는 오셀로 게임.txt", "r")

T = int(input())

dy = [-1,-1,0,1,1,1,0,-1]
dx = [0,1,1,1,0,-1,-1,-1]

for t in range(1,T+1):
    N, M = map(int, input().split())
    # arr = [list(map(int, input().split())) for _ in range(M)]
    pan = [[0]*(N+1) for _ in range(N+1)]
    pan[N//2][N//2], pan[N//2][N//2+1], pan[N//2+1][N//2], pan[N//2+1][N//2+1], = 2,1,1,2

    for _ in range(M):
        x, y, dol = map(int, input().split())
        pan[x][y] = dol

        for i in range(8):
            tx, ty = x + dx[i], y + dy[i]

            while 1 <= tx <= N and 1 <= ty <= N :
                if pan[tx][ty] == 0:
                    break
                if pan[tx][ty] == dol:
                    while tx != x or ty != y:
                        pan[tx][ty] = dol
                        tx, ty = tx - dx[i], ty - dy[i]
                    break

                tx, ty = tx + dx[i], ty + dy[i]

    white = 0
    black = 0
    for i in range(N+1):
        for j in range(N+1):
            if pan[i][j] == 1:
                black += 1
            elif pan[i][j] == 2:
                white += 1
    print(f'#{t} {black} {white}')