class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water=0
        left,right=0,len(heights)-1
        while left<right:
            min_height=min(heights[left],heights[right])
            width=right-left
            water=min_height*width
            max_water=max(max_water,water)
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return max_water            

