import sys
sys.stdin = open("verticalRead.txt","r")

T = int(input())
for tc in range(1,T+1) :
    lst = [list(input()) for i in range(5) ]
    read = ''

    for j in range(len(lst[:][:])) :
        for i in range(5) :
            if len(lst[i][j]) <len(lst[:][:]) :
                j += 1
            read += lst[i][j]

    print(read)