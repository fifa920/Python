import sys
sys.stdin = open("BJ_2667_단지번호붙이기.txt", "r")

N = int(input())

pan = [list(map(int,input())) for _ in range(7)]

def solution(y,x):
    global apt_count
    visited[y][x] = 1

    for i in range(4):
        new_Y = y + dy[i]
        new_X = x + dx[i]

        if 0<= new_X < N and 0<= new_Y < N :
            if pan[new_Y][new_X] == 1 and visited[new_Y][new_X] == 0:
                apt_count += 1
                solution(new_Y,new_X)


visited = [[0]*N for _ in range(N)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
apt_count = 0

for i in range(N):
    for j in range(N):
        if pan[j][i] == 1 and visited[j][i] == 0:
            solution(i,j)
            print(apt_count)
            apt_count = 0
# print(apt_count)
