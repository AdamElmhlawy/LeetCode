import copy
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        matrix1 = copy.deepcopy(matrix)
        for i in range (len(matrix)):
            for j in range (len(matrix[i])):
                matrix1[i][j] = matrix[len(matrix) - (j + 1)][i]
        matrix[:] = matrix1
