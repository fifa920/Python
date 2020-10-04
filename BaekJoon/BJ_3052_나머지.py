import sys
sys.stdin = open("BJ_3052_나머지.txt", "r")

res_list = []

for _ in range(10):
    x = int(input())
    if x % 42 in res_list:
        pass
    else :
        res_list.append(x % 42)

print(len(res_list))