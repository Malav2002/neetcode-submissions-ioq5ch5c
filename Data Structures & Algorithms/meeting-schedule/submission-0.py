"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        currEnd=-1
        for interval in intervals:
            if interval.start < currEnd:
                return False
            currEnd= interval.end
        return True
