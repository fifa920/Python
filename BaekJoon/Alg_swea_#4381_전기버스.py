import sys
sys.stdin = open("Alg_swea_#4381_전기버스.txt", "r")

T = int(input())
for t in range(1,T+1):
    K,N,M = map(int, input().split())
    charges = list(map(int, input().split()))
    charge = [0]*(N+1)
    for i in charges:
        charge[i] = 1
    # print(charge)
    cnt = 0
    bus = 0
    while bus + K < N:
        for i in range(bus+K, bus, -1):
            if charge[i] == 1:
                cnt +=1
                bus = i
                break
        else:
            cnt = 0
            break
    print("#{} {}".format(t,cnt))