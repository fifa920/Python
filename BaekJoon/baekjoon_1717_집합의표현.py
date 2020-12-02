import sys

n,m = map(int, sys.stdin.readline().split())

p = [i for i in range(n+1)]

def find(x):
    if x == p[x]:
        return x
    else :
        p[x] = find(p[x])
    return p[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a != b :
        p[b] = a


for _ in range(m):
    num, a, b = map(int, sys.stdin.readline().split())

    if num == 0 :
        union(a,b)
    else :
        a_p = find(a)
        b_p = find(b)
        if a_p == b_p :
            print('YES')
        else :
            print('NO')