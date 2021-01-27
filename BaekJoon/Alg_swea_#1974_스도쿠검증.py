import sys
sys.stdin = open("Alg_swea_#1974_스도쿠검증.txt", "r")

T = int(input())

def SquareCheck(a,b):
    check_list = [0]*10

    for y in range(3):
        for x in range(3):
            if check_list[pan[a+y][b+x]] == 0:
                check_list[pan[a+y][b+x]] += 1
            else:
                return 1


for t in range(1,T+1):
    pan = [list(map(int, input().split())) for _ in range(9)]
    check = 0

    for y in range(0,9,3):
        for x in range(0,9,3):
            if SquareCheck(y,x) == 1:
                check += 1

