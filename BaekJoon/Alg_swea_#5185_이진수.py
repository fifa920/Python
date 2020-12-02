import sys
sys.stdin = open("Alg_swea_#5185_이진수.txt", "r")


T = int(input())

def Binary(num):
    global temp
    for i in range(4):
        x = num & 1
        temp =str(x)+temp
        num = num >> 1
    return

for t in range(1,T+1):
    N, X = map(str, input().split())
    N = int(N)
    num_dict = {
        '0':0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

    result=''
    for i in range(N):
        temp = ''
        Binary(num_dict[X[i]])
        result = result+temp
    print('#{} {}'.format(t,result))

# def change(num):
#     global lst
#     Q,R = 0,0
#     for i in range(4):
#         Q = num // 2
#         R = num % 2
#         lst[3-i] = R
#         num = Q
#     return
#
# T = int(input())
#
# for t in range(1,T+1):
#     N, X = map(str, input().split())
#     N = int(N)
#     num_dict = {
#         '0':0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
#         'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
#     }
#     result = []
#     for i in range(N):
#         lst = [0] * 4
#         change(num_dict[X[i]])
#         result += lst
#     print('#{} '.format(t), end='')
#     print(*result, sep='')