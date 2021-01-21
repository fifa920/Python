import sys
sys.stdin = open("Alg_swea_#3347_올림픽 종목 투표.txt", "r")

T = int(input())

for t in range(1,T+1):
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    result = [0]*N

    for i in range(M):
        