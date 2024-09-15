class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        first_row = False
        first_col = False
        rows, cols = len(matrix), len(matrix[0])
        first_row = 0 in matrix[0]
        first_col = any(row[0] == 0 for row in matrix)

        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if first_row:
            matrix[0] = [0] * cols

        if first_col:
            for row in matrix:
                row[0] = 0
  =======================================


def markRow(matrix, n, m, i):
    # set all non-zero elements as -1 in the row i:
    for j in range(m):
        if matrix[i][j] != 0:
            matrix[i][j] = -1

def markCol(matrix, n, m, j):
    # set all non-zero elements as -1 in the col j:
    for i in range(n):
        if matrix[i][j] != 0:
            matrix[i][j] = -1

def zeroMatrix(matrix, n, m):
    # Set -1 for rows and cols
    # that contains 0. Don't mark any 0 as -1:
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                markRow(matrix, n, m, i)
                markCol(matrix, n, m, j)
    
    # Finally, mark all -1 as 0:
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == -1:
                matrix[i][j] = 0
    
    return matrix

====================================================================================


def zeroMatrix(matrix, n, m):
    row = [0] * n  # row array
    col = [0] * m  # col array

    # Traverse the matrix:
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                # mark ith index of row wih 1:
                row[i] = 1

                # mark jth index of col wih 1:
                col[j] = 1

    # Finally, mark all (i, j) as 0
    # if row[i] or col[j] is marked with 1.
    for i in range(n):
        for j in range(m):
            if row[i] or col[j]:
                matrix[i][j] = 0

    return matrix
===================================================================

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

 

Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 
