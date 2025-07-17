import heapq

heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 4)
print(heap)  # 输出: [1, 3, 4] (最小元素在第一位)
print(heap[0])

smallest = heapq.heappop(heap)
print(smallest)  # 输出: 1
print(heap)     # 输出: [3, 4]