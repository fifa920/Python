import sys
sys.stdin = open("Alg_swea_#5099_피자 굽기.txt","r")

T = int(input())

for t in range(1,T+1):
    N, M = map(int, input().split())
    chz_list = list(map(int, input().split()))
    print(chz_list)

# T = int(input())
#
# for t in range(1,T+1) :
#     N,M = map(int, input().split())
#     cheese_list = list(map(int, input().split()))
#     Q = []
#     next = 0
#
#     for i in range(N): # 처음에 화덕에 최대 갯수까지만 넣고 시작
#         Q.append([cheese_list[i],i])
#
#     while(len(Q)!=1):
#         if Q[0][0]//2!= 0: # 치즈 녹은 후를 비교
#             Q[0][0] = Q[0][0]//2
#             Q.append(Q.pop(0))
#             continue # 한바퀴 더 돌아야 하니까 continue
#         elif Q[0][0]//2 == 0 and N+next < M : # 여기도 마찬가지로 치즈 녹은 후 비교
#             Q[0][0] = cheese_list[N+next]
#             Q[0][1] = N+next
#             next+=1
#             continue # 한바퀴 더 돌아야 하니까 continue
#         Q.pop(0) # 피자 다 구워졌으면 빼는거
#
#     print('#{} {}'.format(t, Q[0][1]+1))