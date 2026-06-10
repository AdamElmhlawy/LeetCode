class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sett = set(nums)
        set_nums = []
        for num in sett:
            set_nums.append(num)
        print(set_nums)
        print(sett)
        print(nums)
        if len(set_nums) == len(nums):
            return False
        else:
            return True
        