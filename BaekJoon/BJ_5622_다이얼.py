word = input()
alphabet_list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
result = 0

for i in word:
    for j in range(len(alphabet_list)):
        if i in alphabet_list[j] :
            result += j+3
            break

print(result)