class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        n = len(matrix)
        l = 0
        r = n-1

        while l <= r:
            m = l + ((r-l) // 2)

            if target >= matrix[m][0] and target <= matrix[m][-1]:
                nn = len(matrix[m])
                ll = 0
                rr = nn - 1

                while ll <= rr:
                    mm = ll + ((rr - ll) // 2)

                    if target == matrix[m][mm]:
                        return True
                    elif target > matrix[m][mm]:
                        ll = mm + 1
                    else:
                        rr = mm - 1
                return False
            
            elif target > matrix[m][-1]:
                l = m+1
            else:
                r = m-1
        return False