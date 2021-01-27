import sys

sys.stdin = open("Alg_swea_#4839_이진탐색.txt", "r")

T = int(input())


def find(key, start, end):
    cnt = 0
    while start <= end:
        c = (start + end) // 2
        cnt += 1
        if key == c:
            break
        elif key > c:
            start = c
        else:
            end = c
    return cnt


for t in range(1, T + 1):
    P, A, B = map(int, input().split())
    A = find(A, 1, P)
    B = find(B, 1, P)
    if A == B :
        print("#{} 0".format(t))
    elif A > B :
        print("#{} B".format(t))
    else:
        print("#{} A".format(t))

    print(find(A, 1, P), find(B, 1, P))

