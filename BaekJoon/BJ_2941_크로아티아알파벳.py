word = input()

alphabet_list = ['c=','c-','dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for t in alphabet_list:
    word = word.replace(t,'*')

print(len(word))
