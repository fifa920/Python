import sys
sys.stdin = open("BJ_2562_최대값.txt", "r")

check = 0
num_list = []
for _ in range(9):
    x = int(input())
    num_list.append(x)

max_num = num_list[0]

for i in range(9):
    if num_list[i] > max_num :
        max_num = num_list[i]
        check = i

print(max_num, check+1, sep='\n')