import sys
sys.stdin = open("01_45_practice.txt", "r")

def F(X):
    if X == 1 :
        return 1
    if X == 2 :
        return 3
    else :
        return F(X-1) + 2*F(X-2)


T = int(input())

for t in range(1,T+1):
    N = int(input())
    X = N // 10
    print('#{} {}'.format(t, F(X)))
