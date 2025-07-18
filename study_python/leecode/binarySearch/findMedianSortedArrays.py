class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        # 确保 nums1 是较短的数组
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)

        left, right = 0, m
        half_len = (m + n + 1) // 2

        while left <= right:
            partition1 = (left + right) // 2
            partition2 = half_len - partition1

            # 处理边界情况
            max_left1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            min_right1 = float('inf') if partition1 == m else nums1[partition1]

            max_left2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            min_right2 = float('inf') if partition2 == n else nums2[partition2]

            # 检查分割点是否正确
            if max_left1 <= min_right2 and max_left2 <= min_right1:
                # 计算中位数
                if (m + n) % 2 == 1:
                    return max(max_left1, max_left2)
                else:
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
            elif max_left1 > min_right2:
                right = partition1 - 1
            else:
                left = partition1 + 1