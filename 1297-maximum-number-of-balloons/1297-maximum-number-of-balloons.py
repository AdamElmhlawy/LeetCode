class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        balloon = "balloon"
        letters = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}

        for char in text:
            if char in balloon:
                n = letters[char] + 1
                letters[char] = n

        letters["l"] = letters["l"] // 2
        letters["o"] = letters["o"] // 2
        
        return min(letters.values())