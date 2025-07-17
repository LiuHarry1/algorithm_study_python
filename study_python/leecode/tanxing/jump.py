def jump(nums):
    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(len(nums) - 1):  # 不需要遍历最后一个元素
        farthest = max(farthest, i + nums[i])
        if i == current_end:  # 到达当前能到达的最远位置
            jumps += 1
            current_end = farthest
            if current_end >= len(nums) - 1:  # 如果能到达终点
                break
    return jumps


# 测试
nums = [2, 3, 1, 1, 4]
print(jump(nums))  # 输出: 2