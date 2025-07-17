def canJump(nums):

    n = len(nums)
    reach_pos = n-1

    for i in range(n-2, -1, -1):
        if i + nums[i] > reach_pos:
            reach_pos = i

    return reach_pos ==0

def can_jump_new(nums):
    max_reach  = 0
    for i in range(len(nums)):
        if i > max_reach:
            return False

        max_reach = max(max_reach, i + nums[i])
        if max_reach >= len(nums) -1:
            return True
    return True