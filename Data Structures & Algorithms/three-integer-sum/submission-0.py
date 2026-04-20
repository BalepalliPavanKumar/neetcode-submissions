class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=set()
        n=len(nums)
        nums.sort()
        for i in range(n-2):
            j=i+1
            k=n-1
            while j<k:
                temp=nums[i]+nums[j]+nums[k]
                if temp==0:
                    res.add((nums[i],nums[j],nums[k]))
                    j+=1
                elif temp>0:
                    k-=1
                else:
                    j+=1   

        return [list(i) for i in res]             


