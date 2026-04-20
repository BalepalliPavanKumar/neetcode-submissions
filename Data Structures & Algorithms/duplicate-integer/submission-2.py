class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map=defaultdict(int)
        for i in nums:
            hash_map[i]+=1
        for i in hash_map:
            if hash_map[i]>1:
                return True
        return False            