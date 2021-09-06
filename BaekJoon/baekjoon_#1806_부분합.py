import sys

N,S = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

interval_sum, end = 0,0
length = 100001

for start in range(len(lst)):
    while interval_sum < S and end < len(lst):
        interval_sum += lst[end]
        end += 1
    if interval_sum >= S:
        if end-start < length:
            length = end-start
    interval_sum -= lst[start]

if length == 100001:
    print(0)
else:
    print(length)