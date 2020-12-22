import sys
sys.stdin = open('BJ_1541_잃어버린괄호.txt', 'r')

expression = sys.stdin.readline().split('-')
# print(expression)
# N = len(expression)
result = 0


# for i in range(N):
#     hap = 0
#     if '+' in expression[i]:
#         arr = expression[i].split('+')
#         for j in arr :
#             hap += int(j)
#     else :
#         happ = int(expression[i])
#
#
# print(result)

for i in expression[0].split('+'):
    result += int(i)
for i in expression[1:]:
    for j in i.split('+'):
        result = result - int(j)
print(result)