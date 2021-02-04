import sys
sys.stdin = open("Alg_swea_#4613_러시아 국기 같은 깃발.txt", "r")

T = int(input())

for t in range(1,T+1):
    N,M = map(int, input().split())
    pan = [list(input()) for _ in range(N)]
    ans_list = []
    # print(pan)

    for i in range(N-3+1):
        for j in range(i+1, N-2+1):
            ans = 0
            for arr in pan[:i+1]:
                for x in arr:
                    if x != 'W':
                        ans +=1
            # print(ans)
            for arr in pan[i+1:j+1]:
                for x in arr:
                    if x != 'B':
                        ans +=1
            # print(ans)
            for arr in pan[j+1:N]:
                for x in arr:
                    if x != 'R':
                        ans +=1
            # print(ans)
            ans_list.append(ans)

    print(f'#{t} {min(ans_list)}')

