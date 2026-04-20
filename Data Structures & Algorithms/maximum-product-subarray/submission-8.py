class Solution:
    def maxProduct(self, arr: List[int]) -> int:
        max_product=float('-inf')
        for i in range(len(arr)):
            product=1
            for j in range(i,len(arr)):
                product*=arr[j]
                max_product=max(max_product,product)
        return max_product        

