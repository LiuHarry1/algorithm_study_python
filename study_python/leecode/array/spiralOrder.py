"""
54. 螺旋矩阵
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]

输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
"""
def spiralOrder(matrix):

    if not matrix or not matrix[0]:
        return []

    rows, cols = len(matrix), len(matrix[0])
    top, bottom = 0, rows - 1
    left, right = 0, cols - 1
    result = []

    while top <= bottom and left <= right:
        # 从左到右遍历上边界
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        # 从上到下遍历右边界
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            # 从右到左遍历下边界
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        if left <= right:
            # 从下到上遍历左边界
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result




if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = spiralOrder(matrix)
    # [1, 2, 3, 6, 9, 8, 7, 4, 5]
    print(result)
