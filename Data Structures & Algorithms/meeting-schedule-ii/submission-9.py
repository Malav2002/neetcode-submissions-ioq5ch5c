"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        if len(intervals)==1:
            return 1
        intervals.sort(key=lambda x:x.start)
        heap=[]
        heapq.heappush(heap, intervals[0].end)
        for i in range(1,len(intervals)):
            if heap[0] > intervals[i].start:
                heapq.heappush(heap,intervals[i].end)
            else:
                heapq.heappop(heap)
                heapq.heappush(heap, intervals[i].end)
        return len(heap)



