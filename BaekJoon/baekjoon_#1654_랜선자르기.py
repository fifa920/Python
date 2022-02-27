import sys
N,K = map(int, sys.stdin.readline().split())

lines = []
for _ in range(N):
    lines.append(int(sys.stdin.readline()))

start = 1
end = max(lines)

while start <= end:
    mid = (start+end)//2
    target = 0
    for x in lines:
        target += (x//mid)
    if target >= K:
        start = mid+1
    else:
        end = mid-1
print(end)