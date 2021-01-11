T = int(input())

for t in range(1,T+1):
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 길이가 짧은 리스트는 항상 A, 긴 리스트는 항상 B
    if N > M :
        A,B = B,A
        N,M = M,N

    Max = -100000000
    for i in range(M-N+1):
        S = 0
        for j in range(N):
            S += (A[j] * B[i+j])
        Max = max(Max,S)

    print("#{} {}".format(t, Max))
