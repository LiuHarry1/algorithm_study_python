import heapq

def findKthLargest(nums, k):
    # 构建最小堆，堆的大小保持为k
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]

# 示例
nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(findKthLargest(nums, k))  # 输出: 4

import random


def findKthLargest(nums, k):
    def quickselect(left, right, k_smallest):
        if left == right:
            return nums[left]

        pivot_index = random.randint(left, right)

        # 分区操作
        pivot_index = partition(left, right, pivot_index)

        if k_smallest == pivot_index:
            return nums[k_smallest]
        elif k_smallest < pivot_index:
            return quickselect(left, pivot_index - 1, k_smallest)
        else:
            return quickselect(pivot_index + 1, right, k_smallest)

    def partition(left, right, pivot_index):
        pivot = nums[pivot_index]
        # 将pivot移到最右边
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        store_index = left

        for i in range(left, right):
            if nums[i] < pivot:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1

        # 将pivot移到最终位置
        nums[right], nums[store_index] = nums[store_index], nums[right]
        return store_index

    # kth largest就是 (n - k)th smallest
    return quickselect(0, len(nums) - 1, len(nums) - k)


# 示例
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(findKthLargest(nums, k))  # 输出: 5