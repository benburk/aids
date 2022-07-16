"""rotate a matrix counter clockwise 90 degrees"""


def rotate_matrix(mat):
    """rotate a matrix counter clockwise 90 degrees"""
    # Consider all squares one by one
    n = len(mat)
    for i in range(n // 2):

        # Consider elements in group of current square
        for j in range(i, n - 1 - i):
            # store current cell in temp variable
            temp = mat[i][j]
            # move values from right to top
            mat[i][j] = mat[j][n - 1 - i]
            # move values from bottom to right
            mat[j][n - 1 - i] = mat[n - 1 - i][n - 1 - j]
            # move values from left to bottom
            mat[n - 1 - i][n - 1 - j] = mat[n - 1 - j][i]
            # assign temp to left
            mat[n - 1 - j][i] = temp
    return mat


def test():
    """run test cases"""
    mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print(rotate_matrix(mat))


if __name__ == "__main__":
    test()
