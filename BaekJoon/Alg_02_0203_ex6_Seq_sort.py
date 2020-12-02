def seq_sort(x, arr) :

    isYes = False

    for i in range(len(arr)) :
        if arr[i] == x :
            print('입력하신 {0}는 배열 안에 존재합니다.'.format(x))
            isYes = True
    if isYes == False :
        print('배열 안에 존재하지 않습니다.')


arr_1 = [7, 17, 1, 30, 2, 15]
seq_sort(2, arr_1)