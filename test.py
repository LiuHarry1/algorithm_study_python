
def minWindow(s: str, t: str) -> str:

    left =0

    target_count = {}
    for char in t:
        target_count[char] = target_count.get(char, 0) +1

    min_len = float('inf')
    window_count = {}
    formed =0
    required = len(target_count)
    result = ""

    for right in range(len(s)):
        char = s[right]
        window_count[char] = window_count.get(char, 0) + 1

        if char in target_count and window_count[char] == target_count[char]:
            formed +=1

        while left <= right and formed ==required:
            current_len = right -left +1
            if current_len < min_len:
                min_len = min(current_len, min_len)
                result = s[left:right+1]

            left_char = s[left]
            window_count[left_char] -=1
            if left_char in target_count and window_count[left_char] < target_count[left_char]:
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