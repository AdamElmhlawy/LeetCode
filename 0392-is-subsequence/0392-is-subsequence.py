class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        count = 0

        for char in t:
            if s[count] == char:
                count = count + 1

            if count == len(s):
                return True

        return False