class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        spiral_matrix = []
        m = len(matrix)
        n = len(matrix[0])
        top = 0
        bottom = m - 1
        left = 0
        right = n - 1
        while top <= bottom and left <= right:
            #From left to right
            for i in range (left, right + 1):
                spiral_matrix.append(matrix[top][i])
            top += 1    
            #From top to bottom
            for j in range (top, bottom + 1):
                spiral_matrix.append(matrix[j][right])
            right -= 1
            #From right to left
            if top <= bottom:
                for i in range(right, left-1, -1):
                    spiral_matrix.append(matrix[bottom][i])
                bottom -= 1
            #From bottom to top
            if left <= right:
                for j in range (bottom, top-1, -1):
                    spiral_matrix.append(matrix[j][left])
                left += 1


        return spiral_matrix