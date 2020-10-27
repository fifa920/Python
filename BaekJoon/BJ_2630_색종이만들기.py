import sys
sys.stdin = open("BJ_2630_색종이만들기.txt", "r")

N = int(input())
pan = [list(map(int, input().split())) for _ in range(N)]

white = 0
blue = 0

def cut(start_x,start_y,N):
    global white, blue
    check_point = pan[start_x][start_y]
    for i in range(start_x,start_x+N):
        for j in range(start_y,start_y+N):
            if check_point != pan[i][j]:
                cut(start_x, start_y, N//2)             #1사분면
                cut(start_x, start_y+N//2, N//2)        #2사분면
                cut(start_x+N//2, start_y, N//2)        #3사분면
                cut(start_x+N//2, start_y+N//2, N//2)      #4사분면
                return

    if check_point == 0 :
        white += 1
        return
    else :
        blue += 1
        return

cut(0,0,N)
print(white)
print(blue)


