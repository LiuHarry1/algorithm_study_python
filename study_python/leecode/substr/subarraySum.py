class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        pre_sum = 0
        map = {0:1}
        total_count = 0

        for num in nums:
            pre_sum += num
            total_count  += map.get(pre_sum-k, 0)
            if pre_sum in map:
                map[pre_sum] += 1
            else:
                map[pre_sum] = 1
        return total_count


if __name__ == '__main__':
    nums = [1, 1, 1]
    k =2
    solution = Solution()
    result = solution.subarraySum(nums, k)
    print(result)