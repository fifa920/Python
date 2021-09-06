import sys

N,M = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

interval_sum, end, cnt = 0,0,0

for i in range(len(data)):
    while interval_sum < M and end < N:
        interval_sum += data[end]
        end += 1

    if interval_sum == M:
        cnt += 1

    interval_sum -= data[i]

print(cnt)