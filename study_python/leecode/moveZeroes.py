"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作。


示例 1:

输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]
示例 2:

输入: nums = [0]
输出: [0]


"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        right = left = 0

        while right < n :

            if nums[right] !=0:
                nums[left], nums[right] = nums[right] , nums[left]
                left +=1

            right +=1

        return nums


if __name__ == '__main__':
    # nums = [0,1,0,3,12]
    nums = [1,2,3,4]
    solution = Solution()
    result = solution.moveZeroes(nums)
    print(result)