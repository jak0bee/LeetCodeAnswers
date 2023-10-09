import collections


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # In this solution, we aim to find the top k frequent elements in the list 'nums'.
        # We first use the Counter class to count the frequency of each element.
        # We then sort the frequency in ascending order using the sorted function.
        # After sorting, we extract the top k frequent elements by iterating from the end of the sorted frequency list.
        # The time complexity for this solution is O(n log n) where n is the number of unique elements in 'nums'.

        # Calculate frequency of each element and sort by frequency
        frequency = sorted(collections.Counter(nums).items(), key=lambda item: item[1])

        result = []
        # Extract top k frequent elements
        for i in range(len(frequency)):
            if k != 0:
                result.append(frequency[-(i + 1)][0])
                k -= 1

        return result
