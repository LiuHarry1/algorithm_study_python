def threeSum(nums):
    nums.sort()
    n = len(nums)
    result = []
    print(n - 2)
    for i in range(n - 2):
        print(i)
        # Skip duplicate for the first number
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, n - 1
        target = -nums[i]
        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                # Skip duplicates for the second number
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Skip duplicates for the third number
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return result

if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    result = threeSum(nums)
    print(result)

    nums =[0,1,1]
    result = threeSum(nums)
    print(result)