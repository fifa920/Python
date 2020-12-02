import sys
sys.stdin = open("Alg_03_painting.txt","r")

T = int(input())


for t in range(1,T+1) :
    num_color = int(input())
    arr = [[0 for a in range(10)] for b in range(10)]
    count = 0

    for i in range(num_color) :
        startX, startY, endX, endY, color = map(int, input().split())

        for j in range(startX, endX+1) :
            for k in range(startY, endY+1) :
                arr[j][k] += color
                if arr[j][k] == 3:
                    count += 1


    #print(arr)
    print('#{0} {1}'.format(t, count))
    '''for i in range(10):
        print(arr[i])
        print(arr[i].count(3))'''







    '''num_color = int(input())
    for i in range(num_color) :
        arr = list(map(int, input().split()))
    print(arr)'''