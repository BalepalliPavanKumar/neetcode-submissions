class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        rows,cols=len(mat),len(mat[0])
        for i in range(rows):
            for j in range(cols):
                if mat[i][j]==target:
                    return True
        return False            