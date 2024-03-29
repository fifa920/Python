N = int(input())
import math
prime_number = [True]*(N+1)

for i in range(2, int(math.sqrt(N))+1):
    if prime_number[i] == True:
        j=2
        while i*j <= N:
            prime_number[i*j] = False
            j+=1
pn = []
for i in range(2,N+1):
    if prime_number[i]==True:
        pn.append(i)

e, interval_sum = 0,0
cnt = 0
for s in range(len(pn)):
    while interval_sum < N and e < len(pn):
        interval_sum += pn[e]
        e+=1
    if interval_sum == N:
        cnt += 1
    interval_sum -= pn[s]
print(cnt)

# import sys
#
# N = int(sys.stdin.readline())
#
# # N 이하의 소수를 다 뽑아내자
# v = [1] * (N+1)
# m = int(N**0.5)
#
# for x in range(2,m+1):
#     if v[x] == 1:
#         for y in range(x+x, N+1, x):
#             v[y] = 0
# prime_numbers = [i for i in range(2,N+1) if v[i] == 1]
#
# interval_sum, end, cnt = 0, 0, 0
#
# for start in range(len(prime_numbers)):
#     while interval_sum < N  and end < len(prime_numbers):
#         interval_sum += prime_numbers[end]
#         end += 1
#     if interval_sum == N:
#         cnt += 1
#     interval_sum -= prime_numbers[start]
#
# if cnt == 0:
#     print(cnt)
# else:
#     print(cnt)