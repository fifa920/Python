N = int(input())
arr = []

for _ in range(N):
	arr.append(input())
arr=list(set(arr))
res=[]
for x in arr:
	res.append((len(x),x))

res.sort(key=lambda x:(x[0],x[1]))

for x in res:
	print(x[1])
