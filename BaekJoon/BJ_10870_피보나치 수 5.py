N = 5

def fib5(N):
    a, b = 0, 1
    for i in range(N-1):
        a, b = b, a+b
    return b

print(fib5(N))