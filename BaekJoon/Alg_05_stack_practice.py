import sys
sys.stdin = open("stack_practice.txt","r")

Data = input()
stack = []

Info = [0] * 128
Info[ord(')')] = '('
Info[ord(']')] = '['
Info[ord('>')] = '<'
Info[ord('{')] = '}'

howmany = len(Data)

for now in range(howmany) :
    if Data[now] == '(' or Data[now] == '[' or Data[now] == '<' or Data[now] == '{'  :

        stack.append(Data[now])

    elif Info[ord(Data[now])] == stack[-1] :       # Data[now] 는 닫힌 가로가 되는것 / 바로 전의 거와 같으면
        stack.pop(-1)


if stack : print('ERROR')












'''
for now in range(1,4) :
    top += 1
    stack[top] = now
    
while top != -1 :       #스택에 적어도 하나가 있다면
    print(stack[top])
    top -= 1
    '''