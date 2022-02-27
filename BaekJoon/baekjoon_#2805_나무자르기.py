import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

start = 1
end = max(trees)
result = 0

while start <= end:
    mid = (start + end) // 2
    log = 0
    for tree in trees:
        if tree > mid:
            log += (tree-mid)
    if log < M:
        end = mid - 1
    else:
        if mid < result:
            break
        else:
            result = mid
            start = mid + 1

print(result)
#
# def binarySearch(start, end, target):
#     mid = (start + end) // 2
#
#     log = 0
#     for tree in trees:
#         if tree > mid:
#             log += (tree - mid)
#     if log > target:
#         binarySearch(mid + 1, end, target)
#     elif log < target:
#         binarySearch(start, mid - 1, target)
#     else:
#         print(mid)
#         return
#
# binarySearch(1, max(trees), M)