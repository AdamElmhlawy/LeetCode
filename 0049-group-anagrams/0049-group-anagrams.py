from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams_dict  = defaultdict(list)

        for str in strs:
            count = [0] * 26
            for c in str:
                count[ord(c) - ord("a")] += 1

            key = tuple(count)
            anagrams_dict[key].append(str)
        
        return anagrams_dict.values()