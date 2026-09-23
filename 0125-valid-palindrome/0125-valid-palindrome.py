class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0
        r = len(s) - 1

        l_text = ""
        r_text = ""


        while l < len(s) and r >= 0:
            if s[l].isalnum():
                l_text += s[l]
            
            if s[r].isalnum():
                r_text += s[r]

            l += 1
            r -= 1
            
                
        
        cleaned_l = l_text.lower()
        cleaned_r = r_text.lower()

        if cleaned_l == cleaned_r: 
            return True
        return False