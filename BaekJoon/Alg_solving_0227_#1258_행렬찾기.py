import sys
sys.stdin = open('Alg_solving_0227_#1258_행렬찾기.txt', 'r')

T = int(input())

for t in range(1,T+1) :
    n = int(input())
    mat = [list(map(int, input().split())) for _ in range(n)]