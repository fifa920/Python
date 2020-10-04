import sys
sys.stdin = open("BJ_2577_숫자의개수.txt", "r")

A = int(input())
B = int(input())
C = int(input())

num_list = [0]*10
mul = A*B*C

for i in str(mul):
    num_list[int(i)] += 1

print(*num_list, sep='\n')