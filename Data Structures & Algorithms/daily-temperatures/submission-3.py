class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # n=len(temperatures)
        # res=[0]*n
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if temperatures[j]>temperatures[i]:
        #             res[i]=j-i
        #             break
        # return res    

        stack=[]
        n=len(temperatures)
        res=[0]*n
        
        for i in range(n):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                poped=stack.pop()
                res[poped]=i-poped
            stack.append(i)
        return res    



