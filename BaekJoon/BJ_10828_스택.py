import sys
sys.stdin = open("BJ_10828_스택.txt", 'r')
N = int(input())
arr = []


for i in range(N):
    cmd = sys.stdin.readline().strip()
    if cmd.split()[0] == 'push' :
        arr.append(cmd.split()[1])
    elif cmd == 'pop' :
        if len(arr) == 0 :
            print(-1)
        else :
            print(arr.pop())
    elif cmd == 'size' :
        print(len(arr))
    elif cmd == 'empty':
        if len(arr) == 0 :
            print(1)
        else :
            print(0)
    else :
        if len(arr) == 0 :
            print(-1)
        else :
            print(arr[-1])



