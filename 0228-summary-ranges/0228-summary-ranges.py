class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranges = []
        if not nums:
            return ranges

        low = nums[0]
        high = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                high = nums[i]
            else:
                if low == high:
                    ranges.append("{}".format(low))
                else:
                    ranges.append("{}->{}".format(low, high))

                low = nums[i]
                high = nums[i]
            
        if low == high:
            ranges.append("{}".format(low))
        else:
            ranges.append("{}->{}".format(low, high))

        return ranges
        