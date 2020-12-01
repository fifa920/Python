import sys
sys.stdin = open("BJ_7562_나이트의이동.txt", "r")
from collections import deque

# 방향 설정
dy = [-2, -1, 1, 2, 2, 1, -1, -2]
dx = [1, 2, 2, 1, -1, -2, -2, -1]


# BFS 를 이용하여 탐색 시작, 시작점 matrix 자리에 1을 넣고
# 갈 수 있는 조건을 주어 간다면 그 전 값의 +1 해서 간다.
def find(y,x):
    queue = deque()
    queue.append((y,x))
    pan[y][x] = 1

    while queue :
        out_y,out_x = queue.popleft()
        if out_y == end_y and out_x == end_x :
            return pan[out_y][out_x]-1
        for i in range(8):
            new_y = out_y + dy[i]
            new_x = out_x + dx[i]

            if 0<= new_y < N and 0 <= new_x < N and pan[new_y][new_x] == 0 :
                queue.append((new_y,new_x))
                pan[new_y][new_x] = pan[out_y][out_x] + 1


T = int(input())
for _ in range(T):
    N = int(input())
    pan = [[0] * N for _ in range(N)]
    start_y, start_x = map(int, input().split())
    end_y, end_x = map(int, input().split())

    print(find(start_y, start_x))

