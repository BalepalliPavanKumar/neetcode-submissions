class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # water=0
        # n=len(heights)
        # max_water=0
        # for i in range(n):
        #     water=0
        #     for j in range(i+1,n):
        #         width=min(heights[j],heights[i])
        #         water=width*(j-i)
        #         max_water=max(water,max_water)
        # return max_water    

        left,right=0,len(heights)-1
        max_water=0
        while left<right:
            water=0
            min_height=min(heights[left],heights[right])
            width=right-left
            water=min_height*width
            max_water=max(max_water,water)
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return max_water            




