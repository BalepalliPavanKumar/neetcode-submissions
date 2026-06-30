class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canship(capacity):
            d=1
            load=0
            for i in weights:
                if load+i>capacity:
                    d+=1
                    load=i
                else:
                    load+=i
            return d<=days
        left,right=max(weights),sum(weights)
        res=right
        while left<=right:
            mid=(left+right)//2
            if canship(mid):
                ans=mid
                right=mid-1
            else:
                left=mid+1
        return ans            

            
