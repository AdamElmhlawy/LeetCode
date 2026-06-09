class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(intervals)
        if n <= 1:
            return intervals
        intervals = sorted(intervals, key=lambda x: x[0])
        nol_intervals = [intervals[0]]

        for i in range(1, n):
            if intervals[i][0] <= nol_intervals[-1][1]:
                nol_intervals[-1][1] = max(intervals[i][1], nol_intervals[-1][1])
            else:
                nol_intervals.append(intervals[i])

        return nol_intervals