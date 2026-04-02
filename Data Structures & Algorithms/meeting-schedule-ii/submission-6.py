"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals)==0:
            return 0
        if len(intervals)==1:
            return 1

        intervals.sort(key=lambda x: x.start)

        heap = []

        heapq.heappush(heap, intervals[0].end)

        for i in range(1, len(intervals)):
            if intervals[i].start>=heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, intervals[i].end)
        return len(heap)