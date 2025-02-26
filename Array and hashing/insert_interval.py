#Explaination:
# 1. Append the new interval to the intervals list.
# 2. Sort the intervals based on the start time.
# 3. Initialize the answer list with the first interval.
# 4. Iterate through the intervals.
# 5. If the end time of the last interval is greater than the start time of the current interval, then merge the intervals.
# 6. Else, append the current interval to the answer list.

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals = sorted(intervals,key=lambda a:a[0])
        if len(intervals)<2:
            return intervals
        ans = [intervals[0]]
        for i in range(1,len(intervals)):
            if ans[-1][1]>=intervals[i][0]:
                ans[-1][1]=max(ans[-1][1],intervals[i][1])
            else:
                ans.append(intervals[i])
        return ans