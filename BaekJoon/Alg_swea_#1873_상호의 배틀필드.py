import sys
sys.stdin = open("Alg_swea_#1873_상호의 배틀필드.txt", "r")

# U D L R S
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
cmd = {'U':0, 'D':1, 'L':2, 'R':3, 'S':4}
tank = '^v<>'

T = int(input())

for t in range(1,T+1):
    H, W = map(int, input().split())
    pan = []
    # 현재 위치 x,y / 방향 d 를 초기화
    x = y = d = 0
    for i in range(H):
        # 변경하기 위해 string 이 아닌 list로 받는다.
        pan.append(list(input()))
        for j in range(W):
            if pan[i][j] in tank:
                x, y = i, j
                d = tank.index(pan[i][j])
    # print(x,y,d)
    N = int(input())
    cmdStr = input()
    # 명령순으로 반복해서 처리
    for c in cmdStr:
        # 사격일 경우
        if cmd[c] == 4:
            tx, ty = x + dx[d], y + dy[d]
            while 0 <= tx < H and 0 <= ty < W:
                if pan[tx][ty] == '#':
                    break
                if pan[tx][ty] == '*':
                    pan[tx][ty] = '.'
                    break
                tx, ty = tx + dx[d], ty + dy[d]
        # 이동
        else:
            # 방향 전화 후 그 방향으로 전진, but 경계 밖, 벽, 물이면 안됨.
            d = cmd[c]
            pan[x][y] = tank[d]
            tx, ty = x + dx[d], y + dy[d]
            if tx < 0 or tx == H or ty < 0 or ty < W:
                continue
            if pan[tx][ty] == '.':
                pan[tx][ty] = tank[d]
                pan[x][y] = '.'
                x, y = tx, ty
    print(f'#{t}', end=' ')
    for i in pan:
        print(*i)