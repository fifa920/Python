import sys
sys.stdin = open("baekjoon_#4949_균형잡힌세상.txt", "r")

dict = [0] * 128
dict[ord(')')] = '('
dict[ord(']')] = '['


input_list = []

while True :


    sen = list(input())
    #print(sen)
    if sen != ['.'] :
        input_list.extend(sen)
    else :
        break

    #if sen[0] == '.' :
    #    break
stack = []
check_count = 0

for i in range(len(input_list)) :
    if input_list[i] != '.' :
        if input_list[i] == '(' or input_list[i] == '[':
            stack.append(input_list[i])
        elif input_list[i] == ')' or input_list[i] == ']' :
            if len(stack) == 0:
                check_count += 1
            else :
                if dict[ord(input_list[i])] == stack[-1]:
                    stack.pop()
                else :
                    check_count += 1

    else :
        if len(stack) != 0 or check_count != 0:
            print('no')
        else:
            print('yes')
        stack = []
        check_count = 0