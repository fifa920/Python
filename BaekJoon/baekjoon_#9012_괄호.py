import sys
sys.stdin = open("baekjoon_#9012_괄호.txt", "r")

T = int(input())

for t in range(1,T+1) :

    check = 0
    parentheses = input()
    stack = []
    for i in range(len(parentheses)) :
        if parentheses[i] == '(' :
            stack.append(parentheses[i])
        else :
            if len(stack) == 0 :
                check += 1
                break
            else :
                stack.pop()

    if len(stack) != 0 or check == 1 :
        print('NO')
    else :
        print('YES')

