import sys
sys.stdin = open("Alg_swea_#4843_특별한정렬.txt", "r")

T = int(input())

for t in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))


    for i in range(N):
        # 큰값인 index 찾기
        if i % 2 == 0:
            idx = i
            for j in range(i+1,N):
                # 가장 큰 값을 갖는 index를 찾아 idx 에 넣기
                if arr[idx] < arr[j]:
                    idx = j
            # 가장 큰 값을 i 번째 위치로 swap
            arr[i], arr[idx] = arr[idx], arr[i]

        else :
            idx = i
            for j in range(i + 1, N):
                # 가장 작은 값을 갖는 index를 찾아 idx 에 넣기
                if arr[idx] > arr[j]:
                    idx = j
            # 가장 작은 값을 i 번째 위치로 swap
            arr[i], arr[idx] = arr[idx], arr[i]

    print("#{}".format(t), end=' ')
    print(*arr[:10])
