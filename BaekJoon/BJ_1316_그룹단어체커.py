import sys
sys.stdin = open("BJ_1316_그룹단어체커.txt", "r")

N = int(input())
cnt = 0

for t in range(N):
    word = input()

    L = len(word)
    error = 0

    for idx in range(L-1):
        if word[idx] != word[idx+1] :
            new_word = word[idx+1:]
            if word[idx] not in new_word :
                pass
            else :
                error = 1
    if error == 0 :
        cnt += 1
print(cnt)