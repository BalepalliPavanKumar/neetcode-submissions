class Solution:
    def findMin(self, nums: List[int]) -> int:
        # left,right=0,len(nums)-1
        # while left<right:
        #     mid=(left+right)//2
        #     if nums[mid]<nums[right]:
        #         right=mid
        #     else:
        #         left=mid+1
        # return nums[left]
        curr_min=nums[0]
        for i in range(len(nums)):
            if nums[i]<curr_min:
                curr_min=nums[i]
        return curr_min        
