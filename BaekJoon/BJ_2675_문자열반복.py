T = int(input())

for t in range(T):
    N, word = input().split()
    N = int(N)
    for i in range(len(word)):
        print(word[i]*N, end="")
    print()