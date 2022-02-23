import heapq

# it is the min heap implementation
heap = [4,7,3,-2,1,0]

heapq.heapify(heap)
print(heap)

nums = [4,7,3,-2,1,0]
heap2 = []

for value in nums:
	heapq.heappush(heap2, value)
print(heap2)

while heap2:
	print(heapq.heappop(heap2))