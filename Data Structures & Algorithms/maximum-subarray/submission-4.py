class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # total=float('-inf')
        # for i in range(len(nums)):
        #     current=0
        #     for j in range(i,len(nums)):
        #         current+=nums[j]
        #         if current>total:
        #             total=current
        # return total            

        total,current=nums[0],nums[0]
        for i in range(1,len(nums)):
            current=max(current+nums[i],nums[i])
            total=max(total,current)
        return total    