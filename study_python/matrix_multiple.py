
def matrix_multiple(a, b):

    row_a, column_a = len(a), len(a[0])
    row_b, column_b = len(b), len(b[0])

    # 2x3 , 3x2,  2x2
    result_c = [ [ 0 for _ in range(row_a)] for _ in range(column_b) ]

    for i in range(row_a):
        for j in range(column_b):
            for k  in range (column_a):
                result_c[i][j] += a[i][k] * b[k][j]

    return result_c


if __name__ == '__main__':

    a = [
        [1, 2, 3],
        [2,3,4]
    ]

    b = [
        [1, 2],
        [2, 3],
        [5, 1],
    ]

    result = matrix_multiple(a, b)
    print(result)