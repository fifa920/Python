N, M = map(int, input().split())
trees = list(map(int, input().split()))

start = 1
end = max(trees)

while start <= end:
    mid = (start + end) // 2
    log = 0
    for tree in trees:
        if tree > mid:
            log += (tree-mid)
    if log >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)

def binarySearch(start, end, target):
    mid = (start + end) // 2

    log = 0
    for tree in trees:
        if tree > mid:
            log += (tree - mid)
    if log > target:
        binarySearch(mid + 1, end, target)
    elif log < target:
        binarySearch(start, mid - 1, target)
    else:
        print(mid)
        return

binarySearch(1, max(trees), M)