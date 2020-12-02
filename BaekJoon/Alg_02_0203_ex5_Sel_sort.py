def sel_sort (arr) :
    for i in range(0, len(arr)-1) : # 마지막 한 번 전까지 가능
        for j in range(i+1,len(arr)) :
            if arr[i] > arr[j]:
                arr[j], arr[i] = arr[i], arr[j]

    return arr

arr_1 = [7, 9, 1, 5, 3, 2]

print(sel_sort(arr_1))

