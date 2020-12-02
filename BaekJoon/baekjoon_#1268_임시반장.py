import sys
sys.stdin = open("baekjoon_#1268_임반.txt", "r")

N = int(input())
class_table = [list(map(int, input().split())) for _ in range(N)]
stu_table = [[0] * N for _ in range(N)]

for x in range(5) :

    for y in range(N) :
        for z in range(N) :
            if class_table[y][x] == class_table[z][x] and y != z:
                stu_table[y][z] = 1

#print(stu_table)
cnt = []

for i in range(N) :
    cnt.append(stu_table[i][:].count(1))
print(cnt.index(max(cnt)) + 1)