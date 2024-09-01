You are given two strings, coordinate1 and coordinate2, representing the coordinates of a square on an 8 x 8 chessboard.
Return true if these two squares have the same color and false otherwise.

The coordinate will always represent a valid chessboard square. The coordinate will always have the letter first (indicating its column), and the number second (indicating its row).
---------------------------------------------------------------------------------------------
Input: coordinate1 = "a1", coordinate2 = "c3"

Output: true

Explanation:

Both squares are black

-------------------------------------------------------------------------------------------

class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        def convert_column(col):
            return ord(col) - ord('a') + 1
    
        col1, row1 = coordinate1[0], int(coordinate1[1])
        col2, row2 = coordinate2[0], int(coordinate2[1])
        col_num1 = convert_column(col1)
        col_num2 = convert_column(col2)
    
        sum1 = col_num1 + row1
        sum2 = col_num2 + row2
    
        return (sum1 % 2) == (sum2 % 2)
