class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        for i in range(len(min(strs, key=len))):
            first_elements = [row[i] for row in strs]
            if all(element == first_elements[0] for element in first_elements):
                prefix += first_elements[0]
            else:
                break
                
        
        return prefix