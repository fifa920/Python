

import sys
sys.stdin = open("01_45_practice.txt", "r")

def cal_candy(child): # 전체 아이에 대해 각 아이가 가진 사탕의 종류를 다 더해주는 함수
    cnt = 0
    for info in child: # info: 아이가 가지고 있는 사탕 정보
        for num in info: # num: 종류별로 아이가 가지고 있는 사탕 갯수
            if num: # 사탕을 가지고 있다면 count 1 증가
                cnt += 1
    return cnt

def track(child,limit): # depth: 현재까지 배분한 사
    global max_candy
    # limit = 어린이 수가 사탕 수보다 많다면 사탕수만큼, 사탕 수가 어린이 수보다 많다면 어린이 수 만큼
    # 사탕을 모두 배분한 경우
    if  child == limit:
        max_candy = max(max_candy, cal_candy(childs)) # 현재까지 저장된 결과보다 큰 값이 나온다면 결과를 갱신
        return

    for i in range(1,m+1): # 모든 사탕에 대해 조사한다.
        if used[i]: # 이미 배분한 사탕이면 더이상 배분하지 못한다.
            continue
        used[i] = 1 # 배분한 사탕이라고 표시
        childs[child][i] += 1 # 배분받은 아이는 그 사탕을 하나 더 가지게 된다.
        track(child+1,limit) # 다음 아이에게 사탕을 주기 위해 재귀호출
        # 배분하기 전 상태로 다시 바꾸어 준다.
        childs[child][i] -= 1
        used[i] = 0

TCs = int(input())

for tc in range(TCs):
    n,m = map(int,input().split())
    # 각 어린이가 어떤 종류의 사탕을 몇 개 가지고 있는 지를 저장하기 위한 이차원 배열
    childs = [[0 for _ in range(m+1)] for _ in range(n)]
    used = [0 for _ in range(m+1)] # 예비 사탕이 종류별로 하나씩 있다는 것을 처리하기 위한 배열
    max_candy = 0 # 문제에서 요구하는 최대 캔디 종류를 저장할 변수
    limit = min(n,m) # 사탕이 어린이 수보다 적다면 사탕 수 만큼의 깊이로 재귀호출하기 위한 변수
    for i in range(n):
        s = list(map(int,input().split()))
        cnt = s[0] # 어린이가 가지고 있는 사탕 수

        for j in range(1,len(s)):
            childs[i][s[j]] += 1

    track(0,limit)
    print('#%d %d'%(tc+1,max_candy))




# T = int(input())
#
# for t in range(1,T+1):
#     N, M = map(int, input().split())
#     student_list = [list(map(int, input().split())) for _ in range(N)]
#     M_list = [range(1,M+1)]
#     x=0
#
#     if M >= N :
#         for i in range(N):
#             count_list = []
#             for j in range(1,len(student_list[i][:])):
#                 if student_list[i][j] not in count_list :
#                     count_list.append(student_list[i][j])
#
#             if len(count_list) == len(M_list):
#                 x += len(count_list)
#             else :
#                 x += len(count_list)
#                 x += 1
#
#
#     else :
#         for i in range(M):
#             count_list = []
#             for j in range(1, len(student_list[i][:])):
#                 if student_list[i][j] not in count_list:
#                     count_list.append(student_list[i][j])
#             if len(count_list) == len(M_list):
#                 x += len(count_list)
#             else:
#                 x += len(count_list)
#                 x += 1
#
#     print(x)
#
#
