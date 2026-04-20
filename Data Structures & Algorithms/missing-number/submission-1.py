class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        current_sum=sum(nums)
        total_sum=n*(n+1)//2
        return total_sum-current_sum