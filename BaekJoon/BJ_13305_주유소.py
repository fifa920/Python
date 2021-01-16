import sys
sys.stdin = open("BJ_13305_주유소.txt","r")

N = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

Min = min(price[:N])                    # 마지막 가격은 영향을 주지 않기 때문에 :N 인덱싱을 함.
result = 0

# 첫 번째 도시에서 값이 가장 싸기 때문에 처음에 다 넣고 나머지 거리를 가는게 최선
if Min == price[0]:
    result = Min * sum(distance)
else:
    Min = price[0]                      # 처음 도시의 가격을 최소로 잡고
    result = distance[0] * price[0]     # 어차피 두 번째 도시로 가기 위해 처음에는 가격에 상관없이 주유를 해야한다.
    for i in range(1,N-1):
        if price[i] < Min:              # 만약 다음 도시의 가격이 이전 도시의 가격보다 싸면 최소값 경신
            Min = price[i]
        result += Min*distance[i]       # 최소값이 경신되면 거기서 더 넣으면 되고 경신 되지 않으면 이전 값을 계속 유지해서 다음 거리까지는 가서 check하게 된다.
print(result)