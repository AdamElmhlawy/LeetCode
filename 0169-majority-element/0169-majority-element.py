from collections import defaultdict

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        counter = defaultdict(int)

        for num in nums:
            counter[num] += 1
        
        for num in nums:
            if counter[num] > n / 2:
                return num


        