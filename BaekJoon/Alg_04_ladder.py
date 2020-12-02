import sys
sys.stdin = open("Alg_04_ladder.txt", "r")


for t in range(10) :
    N = int(input())
    ladder = [list (map(int, input().split())) for i in range(100)]


    x = 99
    y = ladder[99][:].index(2)


    while True :
        if y-1 > 0 and ladder[x][y-1] == 1 :            # 왼쪽에 길이 있으면
            while y-1 > 0 and ladder[x][y-1] == 1:
                y -= 1
            x -= 1      #계속 왼쪽으로 가다가 길이 없으면 위로 한칸 up
        elif y+1 < 100 and ladder[x][y+1] == 1 :
            while y+1 <100 and ladder[x][y+1] == 1:
                y += 1
            x -= 1      #계속 오른쪽으로 가다가 길이 없으면 위로 한칸 up
        else :
            x -= 1

        if x== 0 :
            break

    print('#{0} {1}'.format(N, y))
