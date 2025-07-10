
# Kadane

def maxSubArray(nums):
    if not nums:
        return 0

    current_max = global_max = nums[0]

    for  i in range(1, len(nums)):
        current_max = max(nums[i] , current_max + nums[i])

        if current_max > global_max:
            global_max = current_max

    return global_max


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    result = maxSubArray(nums)
    print(result)