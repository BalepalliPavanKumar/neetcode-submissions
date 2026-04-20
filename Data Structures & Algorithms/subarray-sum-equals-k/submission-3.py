class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # count=0
        # for i in range(len(nums)):
        #     current_sum=0
        #     for j in range(i,len(nums)):
        #         current_sum+=nums[j]
        #         if current_sum==k:
        #             count+=1
        # return count   
        count=0
        hash_map={0:1}
        cu_sum=0
        for i in nums:
            cu_sum+=i
            if cu_sum-k in hash_map:
                count+=hash_map[cu_sum-k]
            if cu_sum in hash_map:
                hash_map[cu_sum]+=1
            else:
                hash_map[cu_sum]=1  
        return count        

