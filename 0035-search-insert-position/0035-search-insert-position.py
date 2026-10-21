class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n-1
        m = (l+r) // 2

        while l <= r:
            if target == nums[m]:
                return m
            elif target > nums[m]:
                l = m + 1
                m = (l+r) // 2
            else:
                r = m - 1
                m = (l+r) // 2
        return m + 1