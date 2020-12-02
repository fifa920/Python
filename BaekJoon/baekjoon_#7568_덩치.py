import sys
sys.stdin = open ("baekjoon_#7568_덩치.txt", "r")

N = int(input())
stu_list = []
rank_list = [0] * N

for t in range(N) :
    temp_list = list(map(int, input().split()))
    stu_list.append(temp_list)

'''for x in range(2) :
    for y in range(N) :
        if stu_list[y][x] :'''

for i in range(N) :
    k = 1
    for j in range(N) :
        if stu_list[i][0] < stu_list[j][0] and stu_list[i][1] < stu_list[j][1] :
            k += 1
    rank_list[i] = k

print(*rank_list,sep=' ')


