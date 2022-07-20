N = int(input())
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))

lst.sort(key=lambda x:(x[0],x[1]))
for x in range(N):
    print(*lst[x])