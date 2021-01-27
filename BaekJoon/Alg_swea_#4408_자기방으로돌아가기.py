T = int(input())
for t in range(1,T+1):
    N = int(input())
    cnt = [0] * 201

    for _ in range(N):
        s, e = map(int, input().split())
        s = (s+1) // 2
        e = (e+1) // 2

        if s > e:
            s,e = e,s


        for i in range(s,e+1):
            cnt[i] += 1
    print("#{} {}".format(t,max(cnt)))