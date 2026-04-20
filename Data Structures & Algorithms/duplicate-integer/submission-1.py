class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n=set(nums)
        return True if len(n)!=len(nums) else False
        