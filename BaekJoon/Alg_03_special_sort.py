import sys
sys.stdin = open("Alg_03_special_sort.txt","r")



for t in range(3) :
    N = int(input())
    arr = list(map(int, input().split()))
    arr_new = [0 for _ in range(10)]
    max1 = 0
    min1 = 0

    