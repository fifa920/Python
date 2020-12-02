import sys
sys.stdin = open("baekjoon_#2231_분해합.txt", "r")

y = int(input())

numbers = list(range(1,y))

result_list=[]

for x in numbers:
    temp = 0
    N=0
    while True :
        if x // (10**N) == 0 :
            break
        else :
            N += 1
    Q = x
    for n in range(N):
        R = Q % 10
        Q = Q // 10
        temp += R

    if y == temp + x :
        result_list.append(x)

if result_list:
    print(min(result_list))
else :
    print('0')






#
# N = int(input())
# hap_list = [0] * (N+1)
#
# for i in range(1, N+1) :
#     x = 0
#     Q = i
#     while True :
#         R = Q % 10
#         Q = Q // 10
#         x += R
#         if Q == 0 :
#             break
#     hap_list[i] = x+i
#
# if N in hap_list :
#     print(hap_list.index(N))
# else :
#     print('0')