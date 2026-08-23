class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        rows = len(mat)
        for i in range(rows):
            total += mat[i][i]
            if i != rows - 1 - i:
                total += mat[i][rows - 1 - i]
        return total