import sys
sys.stdin = open("baekjoon_#10773_제로.txt","r")

N = int(input())
num_list = []
for i in range(N) :
    x = int(input())
    if x != 0 :
        num_list.append(x)
    elif x == 0 :
        num_list.pop()

print(sum(num_list))