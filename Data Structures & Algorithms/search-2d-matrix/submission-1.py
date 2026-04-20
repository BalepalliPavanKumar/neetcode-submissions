class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        # for i in range(len(mat)):
        #     for j in range(len(mat[0])):
        #         if mat[i][j]==target:
        #             return True
        # return False   

        rows,cols=len(mat),len(mat[0])
        i,j=0,cols-1
        while i<rows and j>=0:
            if mat[i][j]==target:
                return True
            elif mat[i][j]<target:
                i+=1
            else:
                j-=1
        return False                
