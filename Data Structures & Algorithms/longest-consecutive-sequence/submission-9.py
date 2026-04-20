class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # count=1
        # nums.sort()
        # if not nums:
        #     return 0
        # max_element=1    
        # for i in range(1,len(nums)):
        #     if abs(nums[i])-abs(nums[i-1])==1:
        #         count+=1
        #     else:
        #         max_element=max(max_element,count)
        #         count=1
        # return max_element    


        num_set=set(nums)
        maximum=0
        for i in nums:
            if i-1 not in num_set:
                count=1
                current_element=i
                while current_element+1 in num_set:
                    count+=1
                    current_element+=1
                maximum=max(maximum,count)
        return maximum           

          