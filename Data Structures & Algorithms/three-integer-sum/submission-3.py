class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # res=set()
        # nums.sort()
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         for k in range(j+1,len(nums)):
        #             if nums[i]+nums[j]+nums[k]==0:
        #                 temp=[nums[i],nums[j],nums[k]]
        #                 res.add(tuple(temp))
        # return [list(i) for i in res]   

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