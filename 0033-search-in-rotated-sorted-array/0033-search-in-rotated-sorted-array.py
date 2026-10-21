class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if nums[0] > nums[-1]:
            point = 0
            N = len(nums)
            L = 0
            R = N - 1

            while L < R:
                M = (L + R) // 2

                if nums[M] < nums[0]:
                    R = M
                else:
                    L = M + 1

            point = L
            L = 0
            R = point - 1
            while L <= R:
                M = L + ((R-L) // 2)

                if nums[M] == target:
                    return M
                elif target < nums[M]:
                    R = M - 1
                else:
                    L = M + 1
            L = point
            R = N - 1
            while L <= R:
                M = L + ((R-L) // 2)

                if nums[M] == target:
                    return M
                elif target < nums[M]:
                    R = M - 1
                else:
                    L = M + 1
            return -1

        else:
            N = len(nums)
            L = 0
            R = N - 1

            while L <= R:
                M = L + ((R-L) // 2)

                if nums[M] == target:
                    return M
                elif target < nums[M]:
                    R = M - 1
                else:
                    L = M + 1
            return -1