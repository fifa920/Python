# import sys
# sys.stdin = open("baekjoon_#15651_N과M(3).txt", "r")
#
# N, M = map(int, input().split())
# numbers = list(range(1,N+1))
#
# def track(depth, ans) :
#     if depth == M :
#         result = list(map(str, ans))
#         print(' '.join(result))
#         return
#
#     for number in numbers :
#         ans.append(number)
#         track(depth + 1, ans)
#         ans.pop()
#
# track(0,[])

N,M = map(int, input().split())

numbers = [i for i in range(1,N+1)]

def track(depth, ans):
    if depth == M:
        print(*ans)
        return
    for number in numbers:
        ans.append(number)
        track(depth+1, ans)
        ans.pop()

track(0,[])