class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        dp=[[-1]*(amount+1) for _ in range(n)]
        def dfs(i ,amount):
            if amount==0:
                return 0
            if i==n:
                return float('inf')  
            if dp[i][amount]!=-1:
                return dp[i][amount]      
            take=float('inf')
            if coins[i]<=amount:
                take=1+dfs(i,amount-coins[i])
            not_take=dfs(i+1,amount)
            dp[i][amount]= min(take,not_take)
            return dp[i][amount]
        ans=dfs(0,amount)
        if ans==float('inf'):
            return -1
        return ans  