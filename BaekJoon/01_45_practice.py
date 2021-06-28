def arrSum(n, arr):
    if n<=0:
        return 0
    else:
        return arrSum(n-1, arr) + arr[n-1]

arr = [1,2,3,4,5,6,7]
n = len(arr)
result = arrSum(n,arr)
print(result)