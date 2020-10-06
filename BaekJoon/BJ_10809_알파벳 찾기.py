word = input()
result_list = [-1]*26



for i in range(len(word)):
    if result_list[ord(word[i])-97] == -1 :
        result_list[ord(word[i])-97] = i

print(*result_list)

