class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        maximum = 0
        while l < r:
            width = abs(l - r)
            area = min(height[l], height[r]) * width
            if area > maximum:
                maximum = area
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        
        return maximum