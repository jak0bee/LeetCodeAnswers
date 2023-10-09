class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # In this solution, we aim to group the anagrams together.
        # We'll maintain two lists: 'result' for storing groups of anagrams and 'sortedResult' to keep track of sorted versions of strings.
        # By sorting each string, we can easily group anagrams since they'll have the same sorted sequence.
        # As we iterate through 'strs', we check if the sorted version exists in 'sortedResult'.
        # If it does, we append the string to the corresponding group in 'result'. Otherwise, we create a new group.
        # The time complexity for this solution is O(n * m * log(m)), where n is the number of strings and m is the average length of the strings.

        result = []
        sortedResult = []
        for s in strs:
            sorted_s = sorted(s)
            if sorted_s in sortedResult:
                result[sortedResult.index(sorted_s)].append(s)
            else:
                sortedResult.append(sorted_s)
                result.append([s])
        return result
