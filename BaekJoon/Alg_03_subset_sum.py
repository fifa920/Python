import sys
sys.stdin = open('Alg_03_subset_sum.txt','r')

T = int(input())
a = range(1,13)
n = len(a)


for t in range(1,T+1) :
    N, K = map(int,input().split()) # 3 6 / 5 15 / 5 10
    count = 0


    for i in range(1<<n) :
        lst = []
        for j in range(n) :
            if i & (1<<j)  :
                lst.append(a[j])
    print(lst)