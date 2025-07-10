def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    n = len(nums)

    right = [1]*n
    left = [1] * n
    answer = [1] * n

    for i in range(1, n):
        left[i] = left[i-1] * nums[i-1]

    for j in  range(n-2, -1, -1):
        right[j] = right[j+1] * nums[j+1]

    for i in range(n):
        answer = left[i] * right[i];

    return answer



if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    result = productExceptSelf(nums)
    #[24,12,8,6]
    print(result)