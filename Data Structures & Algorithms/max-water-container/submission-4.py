class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water=0
        left,right=0,len(height)-1
        while left<right:
            min_height=min(height[left],height[right])
            width=right-left
            water=min_height*width
            max_water=max(water,max_water)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_water            
              

