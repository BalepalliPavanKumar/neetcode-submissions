class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        hash_map={0:1}
        current_sum=0
        for num in nums:
            current_sum+=num
            if current_sum-k in hash_map:
                count+=hash_map[current_sum-k]
            if current_sum in hash_map:
                hash_map[current_sum]+=1
            else:
                hash_map[current_sum]=1
        return count                

