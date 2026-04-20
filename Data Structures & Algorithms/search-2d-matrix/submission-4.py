class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        m,n=len(mat),len(mat[0])
        i,j=0,n-1
        while i<m and j>=0:
            if mat[i][j]==target:
                return True
            elif mat[i][j]<target:
                i+=1
            else:
                j-=1 
        return False               