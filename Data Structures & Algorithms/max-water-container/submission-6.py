class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left,right=0,len(heights)-1
        max_water=0
        while left<right:
            water=0
            min_height=min(heights[left],heights[right])
            width=right-left
            water=min_height*width
            max_water=max(water,max_water)
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return max_water        




        