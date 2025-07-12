


"""
73. 矩阵置零
 给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。
输入：matrix = [[1,1,1],[1,0,1],[1,1,1]]
输出：[[1,0,1],[0,0,0],[1,0,1]]
 """
def setZeroes( matrix):

    m = len(matrix)
    n = len(matrix[0]) if m >0 else 0


    first_zero_row = any(  matrix[0][i]==0 for i in range(n) )
    first_zero_column = any(matrix[i][0] ==0 for i in range(m))

    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0


    for i in range(1, m):
        if matrix[i][0]==0:
            for j in range(1, n):
                matrix[i][j] =0

    for i in range(1, n):
        if matrix[0][i] == 0:
            for j in range(1, m):
                matrix[j][i] = 0

    if first_zero_row:
        for i in range(n):
            matrix[0][i] = 0

    if first_zero_column:
        for i in range(m):
            matrix[i][0] = 0

    return matrix


if __name__ == '__main__':

    matrix = [[1,1,1],[0,1,1],[1,1,1]]
    result = setZeroes(matrix)
    print(result)

