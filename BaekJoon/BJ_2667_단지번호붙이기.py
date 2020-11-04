import sys
sys.stdin = open("BJ_2667_단지번호붙이기.txt", "r")

N = int(input())

pan = [list(map(int, input())) for _ in range(N)]


def solution(y,x):
    global apt_count
    visited[y][x] = 1

    for i in range(4):
        new_Y = y + dy[i]
        new_X = x + dx[i]

        if 0 <= new_X < N and 0 <= new_Y < N :
            if pan[new_Y][new_X] == 1 and visited[new_Y][new_X] == 0:
                apt_count += 1
                solution(new_Y, new_X)

    return apt_count


visited = [[0]*N for _ in range(N)]

# 12시, 3시, 6시, 9시 순서
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
apt_count = 1
result=[]


for y in range(N):
    for x in range(N):
        if pan[y][x] == 1 and visited[y][x] == 0:
            result.append(solution(y, x))
            apt_count = 1

print(len(result))
for i in sorted(result):
    print(i)
