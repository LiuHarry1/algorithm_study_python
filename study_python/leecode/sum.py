class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        seen_dict = {}

        for i in range(len(nums)):
            curr = nums[i]
            pair_index = seen_dict.get(target - curr)
            if pair_index is not None:
                return [pair_index, i]
            else:
                seen_dict[curr] = i

    def twoSumNew(self, nums , target):

        seen_dict = dict()

        for i, num in enumerate(nums):

            if target - num in seen_dict:
                return [seen_dict[target - num], i ]
            else:
                seen_dict[num] = i

        return []






if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    result = solution.twoSumNew(nums, target)
    print(result)


