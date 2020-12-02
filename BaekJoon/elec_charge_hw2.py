
import sys


sys.stdin = open("4831input.txt","r")

T = int(input())

for tc in range(1, T+1) :
    K, N, M = map(int, input().split())
    charge_stops = [0] + list(map(int, input().split())) + [N]
    charge_count = 0
    last = 0
    next = last + K

    for i in range(1, M+2) :
        if (charge_stops[i] - charge_stops[i-1]) > K :
            charge_count = 0
            break
        if charge_stops[i] > next :
            last = charge_stops[i-1]
            charge_count += 1
        next = last + K

    print("#{0} {1}".format(tc, charge_count))
