class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map={}
        n=len(nums)
        for i in nums:
            if i in hash_map:
                hash_map[i]+=1
            else:
                hash_map[i]=1
        for i in hash_map:
            if hash_map[i]>n/2:
                return i
        return -1                
