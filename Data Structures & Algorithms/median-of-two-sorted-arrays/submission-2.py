class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res=nums1+nums2
        res.sort()
        n=len(res)
        mid=n//2
        if n%2==0:
            return (res[mid-1]+res[mid])/2
        else:
            return res[mid]    