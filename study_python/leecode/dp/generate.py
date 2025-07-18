"""

118. 杨辉三角
"""

def generate(numRows: int) -> list[list[int]]:
    triangle = []

    for row_num in range(numRows):
        # 每一行的第一个和最后一个元素总是1
        row = [1] * (row_num + 1)

        # 计算中间的元素
        for j in range(1, row_num):
            row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]

        triangle.append(row)

    return triangle