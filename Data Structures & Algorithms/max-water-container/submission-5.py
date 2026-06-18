class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water=0
        for i in range(len(heights)):
            water=0
            for j in range(i+1,len(heights)):
                width=j-i
                water=min(heights[i],heights[j])*width
                max_water=max(max_water,water)
        return max_water        

        