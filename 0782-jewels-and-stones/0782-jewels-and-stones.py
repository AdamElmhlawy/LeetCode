class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        jewels_num = 0
        for stone in stones:
            if stone in jewels:
                jewels_num += 1
        
        return jewels_num
        