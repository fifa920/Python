T = int(input())

for i in range(1, T+1):
    x,y = map(int, input().split())
    print('Case #{}: {}'.format(i,x+y))