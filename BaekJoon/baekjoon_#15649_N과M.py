import sys
sys.stdin = open("baekjoon_#15649_N과M.txt", "r")

N, M = map(int, input().split(' '))     # 5 3
numbers = list(range(1, N + 1))     # numbers = [ 1 2 3 4 5 ]


def track(depth, ans) :
    if depth == M:
        result = list(map(str, ans))
        print(' '.join(result))
        return

    for number in numbers:
        if number in ans :
            continue

        else :
            ans.append(number)
            track(depth + 1, ans)
            ans.pop()


track(0,[])