class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # total=nums[0]
        # for i in range(len(nums)):
        #     current_sum=0
        #     for j in range(i+1,len(nums)):
        #         current_sum+=nums[j]
        #         total=max(current_sum,total)
        # return total        

        total=nums[0]
        current_sum=0
        for i in nums:
            current_sum=max(i,current_sum+i)
            total=max(current_sum,total)
        return total    