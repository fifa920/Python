import sys
sys.stdin = open("Alg_swea_#5207_Advanced_이진탐색.txt", "r")

def Binary(l,r,target):



        global count, check
        mid = (l + r) // 2
        k = A_list[mid]
        if l == r:
            if target == A_list[mid]:
                count += 1
            return
        if target == A_list[mid]:
            count += 1
            return
        elif target < A_list[mid] and check != 'left':
            check = 'left'
            Binary(l, mid - 1, target)
        elif target > A_list[mid] and check != 'right':
            check = 'right'
            Binary(mid + 1, r, target)
        else:
            return



T = int(input())

for t in range(1,T+1):
    N, M = map(int, input().split())
    A_list = list(map(int, input().split()))
    B_list = list(map(int, input().split()))
    count = 0




    for target in B_list:
        check = 'default'
        Binary(0, N - 1, target)
    print('#{} {}'.format(t, count))


       