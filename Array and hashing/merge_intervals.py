#Explaination :
# 1. Sort the intervals based on the start time.
# 2. Initialize the answer list with the first interval.
# 3. Iterate through the intervals.
# 4. If the end time of the last interval is greater than the start time of the current interval, then merge the intervals.
# 5. Else, append the current interval to the answer list.
# 6. Return the answer list.

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)<2:
            return intervals
        intervals = sorted(intervals, key=lambda a:a[0])
        ans = [intervals[0]]
        for i in range(1,len(intervals)):
            if ans[-1][1]>=intervals[i][0]:
                ans[-1][1] = max(ans[-1][1],intervals[i][1])
            else:
                ans.append(intervals[i])
        return ans