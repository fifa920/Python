import sys
sys.stdin = open("BJ_8958_OX퀴즈.txt", "r")

T = int(input())

for t in range(T):
    scores_list = list(map(str, input()))
    scores = 0
    cnt = 0
    for x in scores_list:
        if x == 'O' :
            cnt += 1
            scores += cnt
        else :
            cnt = 0
    print(scores)