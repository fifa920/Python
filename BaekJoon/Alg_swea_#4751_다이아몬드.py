import sys
sys.stdin = open("Alg_swea_#4751_다이아몬드.txt", "r")

T = int(input())

for t in range(1,T+1) :
    char = input()
    if len(char) == 1 :
        x = [['..#..'],['.#.#.'],[f'#.{char}.#'],['.#.#.'],['..#..']]
        for i in range(5):
            print(*x[i])
    else :
        y = [['..#..'], ['.#.#.'], [f'#.{char[0]}.#'], ['.#.#.'], ['..#..']]
        for i in range(1, len(char)):
            y[2].extend([f'.{char[i]}.#'])
            for j in range(2):
                if j ==0 :
                    y[j].extend(['.#..'])
                    y[4-j].extend(['.#..'])
                else :
                    y[j].extend(['#.#.'])
                    y[4 - j].extend(['#.#.'])

        #print(y)
        for i in range(5):
            print(''.join(y[i]))

