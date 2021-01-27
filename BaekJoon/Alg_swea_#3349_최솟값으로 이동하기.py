import sys
sys.stdin = open("Alg_swea_#3349_최솟값으로 이동하기.txt", "r")

T = int(input())

for t in range(1,T+1):
    W, H, N = map(int, input().split())
    x, y = map(int, input().split())
    ans = 0

    for _ in range(N-1):
        tx, ty = map(int, input().split())

        if (x - tx)*(y - ty) < 0:
            ans += abs(x - tx) + abs(y - ty)
        elif (x - tx)*(y - ty) >= 0:
            ans += max(abs(x - tx), abs(y - ty))
        x, y = tx, ty
    print("#{} {}".format(t, ans))
