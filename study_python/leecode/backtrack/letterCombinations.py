

"""
17. 电话号码的字母组合

"""
def letterCombinations(digits):
    if not digits:
        return []
    digit_to_letter = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    result = []
    def backtrack(index, path):

        if len(path) ==len(digits):
            result.append("".join(path))
            return

        letters = digit_to_letter[digits[index]]
        for letter in letters:
            path.append(letter)
            backtrack(index+1, path)
            path.pop()

    backtrack(0, [])
    return result




print(letterCombinations("23"))

