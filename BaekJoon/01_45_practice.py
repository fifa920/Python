def quick_sort(arr,start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while (left <= end and arr[left] <= arr[pivot]):
            left += 1
        while (right > start and arr[right] >= arr[pivot]):
            right -= 1
        if left > right:
            arr[pivot], arr[right] = arr[right], arr[pivot]
        else:
            arr[left], arr[right] = arr[right], arr[left]

import math
def is_prime_number(x):
    n = 1000
    arr = [True for i in range(n+1)]

    for i in range(2,int(math.sqrt(x))+1):
        if arr[i] == True:
            j = 2
            while i*j <=n:
                arr[i*j] = False
                j+=1
    return arr
array = is_prime_number(91)
for x in range(2, 92):
    if array[x] :
        print(x, end=' ')