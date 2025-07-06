from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        map = dict()

        for word in strs:

            sorted_word = "".join(sorted(word))

            if map.get(sorted_word):
                map.get(sorted_word).append(word)
            else:
                map[sorted_word] = [word]

        return map.values()


if __name__ == '__main__':
    sol = Solution()

    print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # 输出: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    print(sol.groupAnagrams([""]))
    # 输出: [[""]]

    print(sol.groupAnagrams(["a"]))
    # 输出: [["a"]]