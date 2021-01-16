import sys
sys.stdin = open("BJ_1339_단어수학.txt", "r")

# N = int(input())
# words = []
# alpha = [0]*26
# for _ in range(N):
#     words.append(input())
# # print(words)
# for x in words:
#     n = len(x)
#     i = 10**(n-1)
#     for y in x:
#         alpha[ord(y)-65] = alpha[ord(y)-65] + i
#         i = i // 10
#
# # print(alpha)
# alpha.sort(reverse=True)
# result = 0
#
# for i in range(10):
#     result += alpha[i] * (9-i)
#
# print(result)

lst = [list(map(int, input().split()))  for _ in range(5)]
Max = sum(lst[0])

idx = 0
for i in range(1,5):
    if sum(lst[i]) > Max:
        Max = sum(lst[i])
        idx = i
print(idx+1, Max)