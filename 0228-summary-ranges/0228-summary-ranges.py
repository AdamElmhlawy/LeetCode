class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranges = []
        if nums:
            low = nums[0]
            high = nums[0]
        else:
            return ranges
        for i in range(len(nums)):
            if i < len(nums) - 1:
                if nums[i] + 1 == nums[i + 1]:
                    high = nums[i + 1]
                else:
                    if low == high:
                        ranges.append("{}".format(low))
                        low = nums[i + 1]
                        high = nums[i + 1]
                    else:
                        ranges.append("{}->{}".format(low, high))
                        low = nums[i + 1]
                        high = nums[i + 1]
            
        if low == high:
            ranges.append("{}".format(low))
        else:
            ranges.append("{}->{}".format(low, high))
        return ranges
        