import heapq


class MedianFinder(object):

    def __init__(self):
        # 最大堆（存储较小的一半，用负数实现）
        self.max_heap = []
        # 最小堆（存储较大的一半）
        self.min_heap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # 先将数字加入最大堆
        heapq.heappush(self.max_heap, -num)

        # 确保最大堆的最大值 <= 最小堆的最小值
        if self.min_heap and (-self.max_heap[0] > self.min_heap[0]):
            max_val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, max_val)

        # 平衡两个堆的大小，保持大小差不超过1
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        elif len(self.min_heap) > len(self.max_heap):
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        else:
            return -self.max_heap[0] * 1.0  # 确保返回float