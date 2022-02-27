import heapq, sys

N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

arr.sort(key=lambda x : x[0])

# heap=[arr[0][1]]
heap=[]
heapq.heappush(heap, arr[0][1])

for i in range(1,N):
    if heap[0] > arr[i][0]:
        heapq.heappush(heap, arr[i][1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, arr[i][1])
print(len(heap))