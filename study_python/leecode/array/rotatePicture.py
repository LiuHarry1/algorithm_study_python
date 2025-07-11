
"""
48. 旋转图像
给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。

你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。

原矩阵：
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]

转置后：
[1, 4, 7]
[2, 5, 8]
[3, 6, 9]

水平翻转后：
[7, 4, 1]
[8, 5, 2]
[9, 6, 3]  # 正确结果

"""


def rotate( matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """

    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] =  matrix[j][i], matrix[i][j]


    # for i in range(n):
    #     for j in range(n//2):
    #         matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]

    for row in matrix:
        row.reverse()



if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate(matrix)
    #[[7,4,1],[8,5,2],[9,6,3]]
    print(matrix)