word = input().upper() # 입력 및 대문자화
N = len(word)

result_list = [0]*26
arr = []
for x in word:
    result_list[ord(x)-65] += 1

max_num = max(result_list)

if result_list.count(max_num) == 1:
    print(chr(result_list.index(max_num)+65))
else :
    print('?')