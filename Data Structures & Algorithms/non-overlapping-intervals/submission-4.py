class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count=0
        last=intervals[0][1]
        for start,end in intervals[1:]:
            if start>=last:
                last=end
            else:
                count+=1
                last=min(last,end)    
        return count        