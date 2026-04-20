class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # max_product=float('-inf')
        # for i in range(len(nums)):
        #     product=1
        #     for j in range(i,len(nums)):
        #         product*=nums[j]
        #         max_product=max(max_product,product)
        # return max_product      
        curr_min=curr_max=res=nums[0]
        for i in nums[1:]:
            total=(i,i*curr_min,i*curr_max)
            curr_max=max(total)
            curr_min=min(total)
            res=max(curr_max,res)
        return res    


