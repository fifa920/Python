# sentence = input()
# N = len(sentence)
# cnt = 1
#
# for i in range(1,N-1):
#     if sentence[i+1] != ' ' and sentence[i-1] != ' ' and sentence[i] == ' ' :
#         cnt += 1
#
# print(cnt)

import sys
sys.stdin = open("BJ_1152_단어의개수.txt", "r")
sentence = input().split()
# ex) sentence = The Curious Case of Benjamin Button 일 ㄸ ㅐ sentence = ['The', 'Curious', 'Case', 'of', 'Benjamin', 'Button'] 로 받아진다.

print(sentence)