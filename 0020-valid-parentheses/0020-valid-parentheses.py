class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = []

        for i in range(len(s)):
            if s[i] in "[{(":
                stack.append(s[i])
            else:
                if not stack or pairs[s[i]] != stack[-1]:
                    return False
                stack.pop()
        

        return not stack
        