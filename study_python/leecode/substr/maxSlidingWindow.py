from collections import deque

def maxSlidingWindow(nums, k):
    if not nums or k == 0:
        return []

    q = deque()  # 存储下标
    result = []

    for i in range(len(nums)):
        # 移除过期元素（下标超出窗口左边界）
        while q and q[0] < i - k + 1:
            q.popleft()

        # 维护队列递减性：弹出所有小于当前值的元素
        while q and nums[q[-1]] < nums[i]:
            q.pop()

        q.append(i)

        # 从第 k - 1 个开始记录窗口最大值
        if i >= k - 1:
            result.append(nums[q[0]])

    return result

"""
输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
"""
if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    result = maxSlidingWindow(nums, k)
    print(result)