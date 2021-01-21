import sys
sys.stdin = open("BJ_10828_스택.txt", 'r')
# N = int(input())
# arr = []
#
#
# for i in range(N):
#     cmd = sys.stdin.readline().strip()
#     if cmd.split()[0] == 'push' :
#         arr.append(cmd.split()[1])
#     elif cmd == 'pop' :
#         if len(arr) == 0 :
#             print(-1)
#         else :
#             print(arr.pop())
#     elif cmd == 'size' :
#         print(len(arr))
#     elif cmd == 'empty':
#         if len(arr) == 0 :
#             print(1)
#         else :
#             print(0)
#     else :
#         if len(arr) == 0 :
#             print(-1)
#         else :
#             print(arr[-1])



N = int(input())
stack = []
for _ in range(N):
    command = list(sys.stdin.readline().strip().split())
    if command[0] == 'push':
        stack.append(int(command[1]))
    elif command[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            x = stack.pop()
            print(x)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack) == 0 :
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if len(stack) != 0 :
            print(stack[-1])
        else:
            print(-1)
