class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sett = set(nums)
        if len(sett) == len(nums):
            return False
        else:
            return True
        