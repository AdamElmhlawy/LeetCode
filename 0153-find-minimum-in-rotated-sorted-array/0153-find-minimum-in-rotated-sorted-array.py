class Solution:
    def findMin(self, nums: list[int]) -> int:
        if nums[0] > nums[-1]:
            N = len(nums)
            L = 0
            R = N - 1

            while L < R:
                M = (L + R) // 2

                if nums[M] < nums[0]:
                    R = M
                else:
                    L = M + 1

            return nums[L]
        else:
            return nums[0]