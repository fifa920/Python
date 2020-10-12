# A,B,C = map(int,input().split())
A,B,C = 1000, 70, 170
if B >= C :
    print(-1)
else :
    result = A//(C-B) + 1
    print(result)