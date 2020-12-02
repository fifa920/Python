import sys
sys.stdin = open("Alg_swea_#5356_세로로말해요.txt", "r")

T = int(input())

for t in range(1, T+1):
    pan = [list(map(int,input().split())) for _ in range(5)]
    