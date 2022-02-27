# N, M = 4,2
# numbers = list(range(1, N + 1))
#
#
# def track(depth, ans) :
#     if depth == M:
#         result = list(map(str, ans))
#         print(' '.join(result))
#         return
#     for number in numbers:
#         if number in ans:
#             continue
#         else:
#             ans.append(number)
#             track(depth + 1, ans)
#             ans.pop()
#
#
# track(0,[])

N,M = map(int, input().split())

numbers = [i for i in range(1,N+1)]

def track(depth, ans):
    if depth == M:
        print(*ans)
    for number in numbers:
        if number not in ans:
            ans.append(number)
            track(depth+1, ans)
            ans.pop()
track(0,[])