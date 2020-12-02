import sys
sys.stdin = open("Alg_swea_#5209_Advanced_최소비용.txt", "r")

def find_min(depth):
    global cost

    if min_cost < cost :


T = int(input())

for t in range(1,T+1):
    N = int(input())
    pan = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    min_cost = 10000000000

