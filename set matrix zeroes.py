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
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

 

Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 
