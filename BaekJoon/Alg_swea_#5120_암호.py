import sys
sys.stdin = open("Alg_swea_#5120_암호.txt", "r")

def PW():
    lst = list(map(int, input().split()))
    idx = 0
    for i in range(K):
        idx += M
        if idx ==len(lst):
            x = lst[0]+lst[-1]
            lst.append(x)
        elif idx > len(lst):
            n_idx = ((idx)%len(lst))
            lst[n_idx:n_idx] = [lst[n_idx - 1] + lst[n_idx]]
            idx = n_idx
        else :
            lst[idx:idx] = [lst[idx - 1] + lst[idx]]
    return lst

T = int(input())

for t in range(1,T+1):
    N,M,K = map(int, input().split())
    print('#{}'.format(t), end= ' ')

    print(*PW()[-1:-11:-1])