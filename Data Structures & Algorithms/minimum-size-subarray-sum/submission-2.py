class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # nums.sort()
        # current_sum=0
        min_size=float('inf')
        for i in range(len(nums)):
            current_sum=0
            for j in range(i,len(nums)):
                current_sum+=nums[j]
                if current_sum>=target:
                    min_size=min(min_size,j-i+1)
                    break
        return min_size if min_size!=float('inf') else 0           


