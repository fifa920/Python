N = int(input())
arr = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))
arr.sort()


for target in targets:
    start = 0
    end = N-1
    cnt = 0

    while start <= end:
        mid = (start + end) // 2
        if target == arr[mid]:
            cnt = 1
            print(cnt)
            break
        elif target < arr[mid]:
            end = mid-1
        else:
            start = mid+1
    if cnt == 0:
        print(cnt)

