import sys

T = int(sys.stdin.readline())

for tc in range(T):
    N = int(sys.stdin.readline())
    people = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
    people_sorted = sorted(people, key=lambda x: x[0])
    cnt = 1

    mini = people_sorted[0][1]
    for i in range(1, N):
        if people_sorted[i][1] < mini:
            mini = people_sorted[i][1]
            cnt += 1
    print(cnt)