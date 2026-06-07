class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        lens = len(s)
        roman = {
            "I": 1, 
            "V": 5, 
            "X": 10, 
            "L": 50, 
            "C": 100, 
            "D": 500, 
            "M": 1000
            }
        for i in range(lens):
            num = roman[s[i]]
            next = roman[s[i + 1]] if i < lens - 1 else 0
            if num < next:
                sum -= num
            else:
                sum += num
        return sum