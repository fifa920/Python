<<<<<<< HEAD
# # def quick_sort(arr,start, end):
# #     if start >= end:
# #         return
# #     pivot = start
# #     left = start + 1
# #     right = end
# #     while left <= right:
# #         while (left <= end and arr[left] <= arr[pivot]):
# #             left += 1
# #         while (right > start and arr[right] >= arr[pivot]):
# #             right -= 1
# #         if left > right:
# #             arr[pivot], arr[right] = arr[right], arr[pivot]
# #         else:
# #             arr[left], arr[right] = arr[right], arr[left]
# #
# # import math
# # def is_prime_number(x):
# #     n = 1000
# #     arr = [True for i in range(n+1)]
# #
# #     for i in range(2,int(math.sqrt(x))+1):
# #         if arr[i] == True:
# #             j = 2
# #             while i*j <=n:
# #                 arr[i*j] = False
# #                 j+=1
# #     return arr
# # array = is_prime_number(91)
# # for x in range(2, 92):
# #     if array[x] :
# #         print(x, end=' ')
#
# lst = list('string')
#
# from collections import deque
#
# # N = int(input())
# # cards = [i for i in range(1,N+1)]
# #
# # while len(cards) != 1:
# #     cards.pop(0)
# #     cards.append(cards.pop(0))
# # print(*cards)
#
# # 토마토 7576
# M,N = map(int, input().split())
# pan = []
# for i in range(N):
#     pan.append(list(map(int, input().split())))
# visited = [[0]*M for i in range(N)]
#
# dy = [-1, 0, 1, 0]
# dx = [0, 1, 0, -1]
# ripe = deque()
#
# def bfs(ripe):
#     while ripe:
#         y,x = ripe.popleft()
#         for i in range(4):
#             ny = y + dy[i]
#             nx = x + dx[i]
#             if 0<= ny < N and 0 <= nx < M and pan[ny][nx] == 0 and visited[ny][nx] == 0:
#                 ripe.append((ny,nx))
#                 visited[ny][nx] = 1
#                 pan[ny][nx] = pan[y][x] + 1
#     for x in pan:
#         if 0 in x:
#             return -1
#     return max(max(pan))-1
#
#
# for y in range(N):
#     for x in range(M):
#         if pan[y][x] == 1:
#             ripe.append((y,x))
#             visited[y][x] = 1
#
# print(bfs(ripe))
# # 0이 존재하면 프린트 -1
# # 최대값이 1이면 프린트 0

arr = [7, 5, 9, 0, 3, 1, 6 ,2, 4, 8]
for i in range(1,len(arr)):
    for j in range(i,0,-1):
        if arr[j]<arr[j-1]:
            arr[j],arr[j-1] = arr[j-1],arr[j]
            print(arr)
        else:
            break

=======
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

x= '%.2f' %0.12873126
print(type(x))

dic1 = dict()
dic2 = {}
dic1[1] = 2
dic1[2] = 3
# dic1
dic2 = {i : i*i for i in range(1,10)}
print(dic2)
print(dic2.get(2))
