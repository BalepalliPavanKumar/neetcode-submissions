class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left=0
        res=[]
        for i in range(len(nums)-k+1):
            current_max=float('-inf')
            for j in range(i,i+k):
                current_max=max(current_max,nums[j])
            res.append(current_max)
        return res        
