# def quick_sort(arr,start, end):
#     if start >= end:
#         return
#     pivot = start
#     left = start + 1
#     right = end
#     while left <= right:
#         while (left <= end and arr[left] <= arr[pivot]):
#             left += 1
#         while (right > start and arr[right] >= arr[pivot]):
#             right -= 1
#         if left > right:
#             arr[pivot], arr[right] = arr[right], arr[pivot]
#         else:
#             arr[left], arr[right] = arr[right], arr[left]
#
# import math
# def is_prime_number(x):
#     n = 1000
#     arr = [True for i in range(n+1)]
#
#     for i in range(2,int(math.sqrt(x))+1):
#         if arr[i] == True:
#             j = 2
#             while i*j <=n:
#                 arr[i*j] = False
#                 j+=1
#     return arr
# array = is_prime_number(91)
# for x in range(2, 92):
#     if array[x] :
#         print(x, end=' ')

# import math
#
# n = 1000
# arr = [True for i in range(n+1)]
#
# for i in range(2, int(math.sqrt(n))+1):
#     if arr[i] == True:
#         j = 2
#         while i*j<=n:
#             arr[i*j] = False
#             j += 1
# for i in range(2,n+1):
#     if arr[i]:
#         print(i, end=' ')

# from collections import deque
# q = deque((1,3))
# # q.append((1,3))
# # y,x = q.popleft()
# print(q.popleft())

# N = int(input())
# q = deque([_ for _ in range(1,N+1)])
# while len(q) != 1:
#     q.popleft()
#     q.append(q.popleft())
# print(q[0])

dic1 = dict()
dic2 = {}
dic1[1] = 2
dic1[2] = 3
# dic1
dic2 = {i : i*i for i in range(1,10)}
print(dic2)
print(dic2.get(2))