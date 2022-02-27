from itertools import combinations

N,M = map(int, input().split())
pan = [list(map(int, input().split())) for _ in range(N)]
chickens = []
homes = []
# 치킨집 위치 찾기
for y in range(N):
    for x in range(N):
        if pan[y][x] == 2:
            chickens.append((y,x))
        elif pan[y][x] == 1:
            homes.append((y,x))

total = 10000
for ch in combinations(chickens,M):
    result = 0
    for hy, hx in homes:
        res =10000
        for x in ch:
            res = min((abs(x[0]-hy) + abs(x[1]-hx)), res)
        result += res
    total = min(total, result)
print(total)


