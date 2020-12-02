import sys

sys.stdin = open("List1_dump.txt","r")

Tc = 10

for i in range(1,Tc+1) :
    num_bump = int(input())
    height_list = list(map(int, input().split()))


    for j in range(0,num_bump) :
        if max(height_list) - min(height_list) == 1 :
            print ('#{0} 1'.format(i))
        elif max(height_list) - min(height_list) == 0 :
            print('#{0} 0'.format(i))

        maxH = max(height_list)
        minH = min(height_list)
        maxH -= 1
        minH += 1
        idxMax = height_list.index(max(height_list))
        idxMin = height_list.index(min(height_list))
        height_list[idxMax] = maxH
        height_list[idxMin] = minH



    result = max(height_list)-min(height_list)

    print('#{0} {1}'.format(i,result))

