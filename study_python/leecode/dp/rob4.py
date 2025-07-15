"""

2560. 打家劫舍 IV
"""

def minCapability(nums, k):
    left = min(nums)
    right = max(nums)

    def isPossible(cap):
        count = 0
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] <= cap:
                count += 1
                i += 2  # 跳过下一个房子
            else:
                i += 1
            if count >= k:
                return True
        return count >= k

    while left < right:
        mid = (left + right) // 2
        if isPossible(mid):
            right = mid
        else:
            left = mid + 1
    return left