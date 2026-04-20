class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        rows,cols=len(mat),len(mat[0])
        left,right=0,rows*cols-1
        while left<=right:
            mid=(left+right)//2
            mid_value=mat[mid//cols][mid%cols]
            if mid_value==target:
                return True
            elif mid_value<target:
                left=mid+1
            else:
                right=mid-1 
        return False               