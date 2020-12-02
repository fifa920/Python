import sys
sys.stdin = open("baekjoon_#10448_유레카이론.txt", "r")

N = int(input())
depth=3
ans=[]
result=[]

def track(ans,r):
    if r == depth :
        result.append(sum(ans))
        if K in result:
            print(1)
        else :
            print(0)
        # if sum(ans) == K :
        #
        # else:
    else :
        for i in T_list:
            ans.append(i)
            track(ans, r+1)
            ans.pop()

for _ in range(N):
    K = int(input())
    T_list = []
    for i in range(1,K):
        if i*(i+1)/2 < K :
            T_list.append(int(i*(i+1)/2))
    track([],0)