class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) - 1

        while left <= right:
            if numbers[left] + numbers[right] == target:
                result = [left + 1, right + 1]
                return result

            else:
                if numbers[left] + numbers[right] > target:
                    if numbers[right] == numbers[right - 1]:
                        while numbers[right] == numbers[right - 1]: right -= 1
                    else:
                        right -= 1
                if numbers[left] + numbers[right] < target:
                    if numbers[left] == numbers[left + 1]:
                        while numbers[left] == numbers[left + 1]: left += 1
                    else:
                        left += 1
