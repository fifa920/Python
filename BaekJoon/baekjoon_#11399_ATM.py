N = int(input())
arr = list(map(int, input().split()))

arr.sort()
result = 0

for x in range(N):
    result += arr[x]*(N-x)

print(result)