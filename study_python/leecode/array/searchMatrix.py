def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    if not matrix or not matrix[0]:
        return False

    m, n = len(matrix), len(matrix[0])
    row, col = 0, n - 1  # 从右上角开始

    while row < m and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            col -= 1  # 向左移动
        else:
            row += 1  # 向下移动

    return False


if __name__ == '__main__':
    matrix = [[1, 4, 7, 11, 15],[2, 5, 8, 12, 19], [3, 6, 9, 16, 22],[10, 13, 14, 17, 24],  [18, 21, 23, 26, 30]]
    target = 5

    result = searchMatrix(matrix, target)

    print(result)