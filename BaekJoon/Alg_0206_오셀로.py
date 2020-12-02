import sys
sys.stdin = open("Alg_0206_오셀로.txt","r")

T = int(input())
N , M = map(int, input().split())       # 4x4 / 12번 돌을 놓음

pan = [[0 for _ in range(N)] for _ in range(N)] # 1: 흑, 2: 백
pan[1][1] , pan[2][1], pan[1][2], pan[2][2] = 2, 2, 1, 1
print(pan)


