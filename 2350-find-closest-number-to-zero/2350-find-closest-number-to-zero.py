class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lowest = nums[0]
        for num in nums:
            if abs(num) < abs(lowest):
                lowest = num
            if num == abs(lowest) and num > lowest:
                lowest = num

        return lowest