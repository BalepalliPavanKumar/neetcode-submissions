class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]
        # return [-1]     \
        m={}
        for i in range(len(nums)):
            compliment=target-nums[i]
            if compliment in m:
                return [m[compliment],i]
            m[nums[i]]=i    
        return [-1]        

