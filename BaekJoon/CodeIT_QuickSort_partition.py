# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    a, b = my_list[index2], my_list[index1]
    my_list[index2], my_list[index1] = b, a



# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    b = start
    N = len(my_list)
    pivot = my_list[end]
    for i in range(N - 1):
        if my_list[i] > pivot:
            pass
        else:
            swap_elements(my_list, b, i)
            b += 1
    swap_elements(my_list, end, b)
    return b

    # 코드를 작성하세요.


# 테스트 1
list1 = [4, 3, 6, 2, 7, 1, 5]
pivot_index1 = partition(list1, 0, len(list1) - 1)
print(list1)
print(pivot_index1)

# 테스트 2
list2 = [6, 1, 2, 6, 3, 5, 4]
pivot_index2 = partition(list2, 0, len(list2) - 1)
print(list2)
print(pivot_index2)
