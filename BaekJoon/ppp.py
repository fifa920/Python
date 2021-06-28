from collections import deque
dy = [-1, 0, 1, -1]
dx = [0, 1, 0, -1]


def solution(garden):
    # 여기에 코드를 작성해주세요.
    answer = 0
    N = len(garden)
    q = deque()

    for i in range(N):
        for j in range(N):
            if garden[i][j]:
                q.append((i, j))

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0 <= nx < N and garden[ny][nx] == 0:
                garden[ny][nx] = 1
                q.append((ny, nx))
        answer += 1

    return answer


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
garden1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
ret1 = solution(garden1)
print("solution 함수의 반환 값은", ret1, "입니다.")