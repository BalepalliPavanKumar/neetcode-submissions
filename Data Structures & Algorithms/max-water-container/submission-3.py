class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # water=0
        # left,right=0,len(heights)-1
        # while left<right:
        max_water=0
        for i in range(len(heights)):
            water=0
            for j in range(i+1,len(heights)):
                width=j-i
                min_height=min(heights[i],heights[j])
                water=min_height*width
                max_water=max(max_water,water)
        return max_water        

