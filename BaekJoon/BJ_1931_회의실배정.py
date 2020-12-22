import sys
N = int(sys.stdin.readline().rstrip())
time_list = []
for _ in range(N):
    time_list.append(list(map(int, sys.stdin.readline().split())))

sorted_list = list(sorted(time_list, key = lambda x: (x[1], x[0])))
# print(sorted_list)

cnt = 1
prev_time = sorted_list[0][1]

for i in range(1, N):
    if sorted_list[i][0] >= prev_time :
        cnt += 1
        prev_time = sorted_list[i][1]

print(cnt)