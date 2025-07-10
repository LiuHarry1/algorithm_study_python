def minWindow(s: str, t: str) -> str:
    if not s or not t or len(s) < len(t):
        return ""

    target_counts = {}
    for char in t:
        target_counts[char] = target_counts.get(char, 0) +1


    required= len(target_counts)
    formed = 0
    window_counts ={}

    # 滑动窗口指针和结果变量
    left = 0
    min_len =float('inf')
    result = ""

    for right in range(len(s)):
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) +1

        # 如果当前字符在t中，并且窗口中的数量达到了目标数量
        if char in target_counts and target_counts[char] == window_counts[char]:
            formed +=1

        # 尝试收缩窗口左边界
        while left <= right and formed == required:

            # 更新最小窗口
            current_len =right -left +1
            if current_len < min_len:
                min_len = current_len
                result = s[left:right+1]

            # 移动左指针
            left_char = s[left]
            window_counts[left_char] -=1
            if left_char in target_counts and window_counts[left_char] <target_counts[left_char]:
                formed -=1

            left +=1



    return result

# 测试示例
if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    print(minWindow(s, t))  # 输出: "BANC"

    s = "a"
    t = "a"
    print(minWindow(s, t))  # 输出: "a"
    #
    # s = "a"
    # t = "aa"
    # print(minWindow(s, t))  # 输出: ""