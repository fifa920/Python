N = int(input())
weight_list = []

for _ in range(N):
    weight_list.append(int(input()))
weight_list.sort(reverse=True)


for i in range(N):
    weight_list[i] = weight_list[i] * (i+1)
print(max(weight_list))