class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ans=1
        left,right=1,max(piles)
        while left<=right:
            mid=(left+right)//2
            hours=0
            for i in piles:
                hours+=math.ceil(i/mid)
            if hours<=h:
                ans=mid
                right=mid-1
            else:
                left=mid+1
        return ans        

