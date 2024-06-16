# https://leetcode.com/problems/set-matrix-zeroes/description/

def setZeroes(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    # Time Complexity:  O(mn)
    # Space Complexity: O(m+n)
    
    # Keep track of row and column that needs to be set to 0s
    row_map = []
    col_map = []

    row_len = len(matrix)
    col_len = len(matrix[0])
    
    for i in range(row_len):
        for j in range(col_len):
            # If an element is 0, add its row/col to the map
            if matrix[i][j] == 0:
                if i not in row_map:
                    row_map.append(i)
                if j not in col_map:
                    col_map.append(j)
    
    # Set elements in row_map to 0
    for row in row_map:
        for col in range(col_len):
            matrix[row][col] = 0
    
    # Set elements in col_map to 0
    for col in col_map:
        for row in range(row_len):
            matrix[row][col] = 0
    