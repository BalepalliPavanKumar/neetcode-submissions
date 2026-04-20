class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==target:
                    return True
        return False            