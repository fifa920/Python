import sys
sys.stdin = open("Alg_03_hw_pascal.txt","r")

T = int(input()) # 1
N = int(input()) # 4
lst = []
for i in range(1, N+1) :
    lst.append(list([0]* i))

for i in range(N) :
    lst[i][0] = 1
    if i >= 1 :
        lst[i][i] = 1

for i in range(2,N) :
    for j in range(1, N-2) :
        lst[i][j] = lst[i-1][j-1]+lst[i-1][j]


print(lst)