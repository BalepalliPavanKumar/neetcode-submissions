class Solution:
    def trap(self, height: List[int]) -> int:
        # max_water=0
        # n=len(height)
        # for i in range(n):
        #     left_max=0
        #     right_max=0
        #     for j in range(i,-1,-1):
        #         left_max=max(left_max,height[j])
        #     for j in range(i,n):
        #         right_max=max(right_max,height[j])
        #     max_water+=min(left_max,right_max)-height[i]
        # return max_water   
        water=0
        left,right=0,len(height)-1
        max_left,max_right=height[left],height[right]
        while left<right:
            if max_left<max_right:
                left+=1
                max_left=max(max_left,height[left])
                water+=max_left-height[left]
            else:
                right-=1
                max_right=max(max_right,height[right])
                water+=max_right-height[right]
        return water            




