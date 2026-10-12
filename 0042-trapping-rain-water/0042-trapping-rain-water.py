class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)

        max_l = max_r = 0

        max_left = [0] * n
        max_right = [0] * n

        for i in range(n):
            j = -i -1

            max_left[i] = max_l
            max_right[j] = max_r
            
            max_l = max(height[i], max_l)
            max_r = max(height[j], max_r)
        

        summ = 0
        for i in range(n):
            pot = min(max_left[i], max_right[i])
            summ += max(0, pot - height[i])
        
        return summ