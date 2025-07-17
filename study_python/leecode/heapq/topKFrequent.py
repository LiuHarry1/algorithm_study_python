
from collections import Counter
import heapq

def topKFrequent(nums, k):
    count = Counter(nums)
    heap = []

    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) >k:
            heapq.heappop(heap)

    return [num  for freq, num in heap]

def topKFrequent_new(nums, k):
    # 手动统计频率
    freq_map = {}
    for num in nums:
        freq_map[num] = freq_map.get(num, 0) + 1

    # 创建桶
    max_freq = max(freq_map.values()) if freq_map else 0
    buckets = [[] for _ in range(max_freq + 1)]

    for num, freq in freq_map.items():
        buckets[freq].append(num)

    # 收集结果
    result = []
    for freq in range(max_freq, -1, -1):
        result.extend(buckets[freq])
        if len(result) >= k:
            break

    return result[:k]



if __name__ == '__main__':

    nums = [1,1,1,2,2,3,3,3,3]
    k = 2
    print(topKFrequent(nums, k))  # 输出: [3, 1]