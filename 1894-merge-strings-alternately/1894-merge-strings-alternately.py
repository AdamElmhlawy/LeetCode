class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        string = ""
        len1 = len(word1)
        len2 = len(word2)
        if len1 == len2:
            for i in range(len1):
                string += word1[i]
                string += word2[i]
        elif len1 > len2:
            for i in range(len2):
                string += word1[i]
                string += word2[i]
            for j in range(i + 1, len1):
                string += word1[j]
        elif len1 < len2:
            for i in range(len1):
                string += word1[i]
                string += word2[i]
            for j in range(i + 1, len2):
                string += word2[j]
        return string
        