class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # hash_map=defaultdict(int)
        # for i in nums:
        #     hash_map[i]+=1
        #     if hash_map[i]>1:
        #         return i    

        hash_map={}
        for i in nums:
            if i in hash_map:
                hash_map[i]+=1
            else:
                hash_map[i]=1
        for key,val in hash_map.items():
            if val>1:
                return key            