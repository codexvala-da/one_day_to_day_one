#Exaplantion:
# 1. Sort the intervals based on the start time
# 2. Initialize the answer list with the first interval
# 3. Iterate through the intervals
# 4. If the end time of the last interval is greater than the start time of the current interval, then merge the intervals
# 5. Else, append the current interval to the answer list
# 6. Return the answer list

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals,key=lambda a:a[0])
        if len(intervals)<2:
            return 0
        ans = [intervals[0]]
        count = 0
        for i in range(1,len(intervals)):
            if ans[-1][1]>intervals[i][0]:
                ans[-1][1] = min(ans[-1][1],intervals[i][1])
                count+=1
            else:
                ans.append(intervals[i])
        return count