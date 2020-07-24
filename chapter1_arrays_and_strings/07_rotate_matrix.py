testcase = [
    [1,2,3,4],
    [2,3,5,7],
    [9,4,2,1],
    [5,4,2,6]
]

transposed = [
    [5,9,2,1],
    [4,4,3,2],
    [2,2,5,3],
    [6,1,7,4]
]

def rotate_matrix(matrix):
    matrix_size = len(matrix)
    rotated = [ [None] * matrix_size for i in range(matrix_size) ]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            rotated[i][j] = matrix[matrix_size-1-j][i]

    return rotated;

print(rotate_matrix(testcase))
