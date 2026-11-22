class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numset = set(nums)
        longest = 0

        for num in numset:
            if num - 1 not in numset:
                next_num = num + 1
                length = 1
                
                while next_num in numset:
                    length += 1
                    next_num += 1
                longest = max(longest, length)
        
        return longest