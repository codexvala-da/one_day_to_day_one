# Given an array of meeting time interval objects consisting of start and 
# end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), find the minimum number of days 
# required to schedule all meetings without any conflicts.

#Explaination:
# 1. Sort the intervals based on the start time.
# 2. Initialize the min_heap list.
# 3. Iterate through the intervals.
# 4. If the end time of the first element of the min_heap is less than or equal to the start time of the current interval, then pop the first element.
# 5. Push the end time of the current interval to the min_heap.
# 6. Return the length of the min_heap.

import heapq
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals = sorted(intervals,key=lambda a:a.start)
        min_heap = []
        for i in intervals:
            if min_heap and min_heap[0] <= i.start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap,i.end)
        return len(min_heap)