# def fib(n) :
#     if n<=1 :
#         return n
#     else :
#         return fib(n-1) + fib(n-2)
#
# for i in range(101):
#     print(fib(i), end=" ")

# 너무 비효율적이다, 같은 함수를 너무 많이 꺼내쓴다.
# SOL)
# 미리 찾아서 다 리스트에 넣자 !

def fib2(n) :
    f = [0] * (n+1)
    if n > 0 :
        f[1] = 1
        for i in range(2,n+1) :
            f[i] = f[i-1] + f[i-2]
    return f[n]

for i in range(15):
    print(fib2(i), end=" ")