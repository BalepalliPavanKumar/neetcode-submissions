class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hash_map=defaultdict(int)
        for i in nums:
            hash_map[i]+=1
            if hash_map[i]>1:
                return i    