class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for char in ransomNote:
            if char in magazine:
                ransomNote = ransomNote.replace(char, "", 1)
                magazine = magazine.replace(char, "", 1)
        
        if ransomNote:
            return False
        else:
            return True
        