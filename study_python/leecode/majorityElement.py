class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        return candidate


if __name__ == '__main__':
    sol = Solution()

    # print(sol.majorityElement([3, 2, 3]))  # 输出: 3
    # print(sol.majorityElement([2, 2, 1, 1, 1, 2, 2]))  # 输出: 2
    print(sol.majorityElement([1, 3, 3]))  # 输出: 1
