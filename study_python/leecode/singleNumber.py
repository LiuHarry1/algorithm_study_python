class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            result ^= num
        return result


if __name__ == '__main__':
    sol = Solution()

    # print(sol.singleNumber([2, 2, 1]))  # 输出: 1
    print(sol.singleNumber([4, 1, 2, 1, 2]))  # 输出: 4
    print(sol.singleNumber([1]))  # 输出: 1