
"""
213. 打家劫舍 II

"""
def rob(self, nums):

    def rob_helper(sub_nums):

        pre_max =0
        cur_max = 0

        for num in sub_nums:
            tmp = cur_max
            cur_max = max(pre_max +num, cur_max)
            pre_max = tmp

        return cur_max

    if not nums:
        return 0

    if len(nums) == 1:
        return nums[0]

    return max(rob_helper(nums[1:]), rob_helper(nums[:-1]))