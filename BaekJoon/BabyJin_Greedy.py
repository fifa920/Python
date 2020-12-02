#num = 456789
num = int(input('숫자를 입력하세요 : '))
c = [0] * 12 # 12 개의 리스트를 만드는 이유 : i+1, i+2 까지 비교하므로 syntax 오류를 막기 위한 것.
for i in range(6) :
    c[num % 10] += 1
    num //= 10
i = 0
tri = run = 0
while i<10 :
    if c[i] >= 3: # triplet 검사 first
        c[i] -= 3
        tri += 1
        continue
    if c[i] >= 1 and c[i+1] >=1 and c[i+2] >= 1 : # run 검사 second
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        run += 1
        continue
    i += 1

if run + tri == 2 : 
    print("Baby Jin")
else :
    print("Not baby Jin")