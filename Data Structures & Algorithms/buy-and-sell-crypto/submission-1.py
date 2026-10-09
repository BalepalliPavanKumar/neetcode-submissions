class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        for i in range(len(prices)):
            current=float('-inf')
            for j in range(i+1,len(prices)):
                current=prices[j]-prices[i]
                res=max(current,res)
        return res        
                

