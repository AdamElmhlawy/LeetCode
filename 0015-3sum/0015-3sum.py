class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = []
        chosen = set()
        nums.sort()

        for i in range(len(nums)):
            target = -nums[i]
            visited = {}
            for j in range(i + 1, len(nums)):
                k = target - nums[j]

                if k in visited:
                    if (nums[i], nums[visited[k]], nums[j]) not in chosen:
                        output.append([nums[i], nums[visited[k]], nums[j]])
                        chosen.add(((nums[i], nums[visited[k]], nums[j])))
                else:
                    visited[nums[j]] = j
        
        return output
