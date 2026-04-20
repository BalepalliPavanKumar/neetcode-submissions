class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water=0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                min_height=min(heights[i],heights[j])
                width=j-i
                water=min_height*width
                max_water=max(max_water,water)
        return max_water        


