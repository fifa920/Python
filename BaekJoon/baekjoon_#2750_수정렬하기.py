N = int(input())
arr = []

for _ in range(N):
    arr.append(int(input()))

for i in range(len(arr)):
    for j in range(1,len(arr)):
        if arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
            # print(arr)

for n in arr:
    print(n)