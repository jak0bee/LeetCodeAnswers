class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        #Create a hashmap where the key is the sorted string of this anagram and the values are the anagrams
        result = {}
        for s in strs:
            sorted_s = str(sorted(s))
            if sorted_s in result.keys():
                result[sorted_s].append(s)
            else:
                result[sorted_s] = [s]
        return result.values()