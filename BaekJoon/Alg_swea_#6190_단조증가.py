import sys
sys.stdin = open("Alg_swea_#6190_단조증가.txt", "r")

T = int(input())
for t in range(1,T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    ans = -1
    numbers.sort(reverse = True)
    # 개의 값들에서 2개 선택해서 곱하는 모든 경우
    for i in range(N-1):
        for j in range(i+1,N):
            check = numbers[i]*numbers[j]
            # 내림차순 정렬되어 있으므로
            if ans >= check :
                break
            # 출력 시 단조증가인 것을 판단한다 만약 없으면 -1 출력
            t = check
            b = t % 10
            t //= 10
            while t != 0:
                a = t % 10
                if a > b:
                    break
                t //= 10
                b = a
            else:
                ans = max(ans,check)
    print(ans)