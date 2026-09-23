class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        i = 0
        j = 0

        while left <= right:
            i = s[left]
            j = s[right]
            s[left] = j
            s[right] = i
            left += 1
            right -= 1
        
        return s