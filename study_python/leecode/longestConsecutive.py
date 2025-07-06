class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        num_set = set(nums)

        longest= 0

        for num in num_set:

            if num - 1 not in num_set:
                current = num
                streak = 1

                while current +1 in num_set:
                    current +=1
                    streak +=1

                longest =max(longest, streak)

        return longest


if __name__ == '__main__':
    sol = Solution()

    print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))  # 输出: 4 ([1, 2, 3, 4])
    print(sol.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 输出: 9 ([0,1,2,3,4,5,6,7,8])
    print(sol.longestConsecutive([1, 0, 1, 2]))  # 输出: 3 ([0,1,2])
    print(sol.longestConsecutive([]))  # 输出: 0
