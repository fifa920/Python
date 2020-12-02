import sys
sys.stdin = open("Alg_03_hw_danjo.txt", "r")

T = int(input())

for t in range(T) :
    N = int(input())
    numbers = list(map(int, input().split()))
    arr = []
    rest_list = []      # 각 자리 숫자들을 담는 리스트



    for i in range(len(numbers)) :
        for j in range(i+1,len(numbers)) :
            temp = numbers[i] * numbers[j]

            str_temp = str(temp)
            for k in range(len(str_temp)-1) :
                rest_list.append(str_temp)
                if str_temp[k] <= str_temp[k+1] :
                    arr.append(temp)

    print('#{0} {1}'.format(t, max(arr)))