import sys
sys.stdin = open("Alg_Solving_0206_#5356_세로로말해.txt", "r")

T = int(input())

for t in range(1,T+1) :
    arr = []
    result = []
    for i in range(5):
        str_arr = str(input() + '#################')
        arr.append(str_arr)
    #print(arr)


    for a in range(15):
        for b in range(5):
            if arr[b][a] != '#':
                result.append(arr[b][a])
    print('#{} {}'.format(t, ''.join(result)))
    #print('#%d ' % (tc) + ''.join(result))