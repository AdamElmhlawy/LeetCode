class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l_s = []
        l_t = []
        for char in s:
            l_s.append(char)
        for char in t:
            l_t.append(char)
        
        if sorted(l_s) == sorted(l_t):
            return True
        else:
            return False