import sys
sys.stdin = open('BJ_11047_동전0.txt', 'r')

N,K = map(int, input().split())
coins = []
target = 0
for i in range(N):
    coins.append(int(input()))

for i in range(N-1,-1,-1):
    if K // coins[i] != 0 :
       target +=  K // coins[i]
       K %= coins[i]
print(target)