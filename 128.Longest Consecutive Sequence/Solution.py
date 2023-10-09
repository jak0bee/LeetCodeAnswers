class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # In this solution, we aim to find the longest consecutive sequence in an unsorted list of numbers.
        # Instead of sorting, which would take O(n * log(n)) time, we utilize a set for O(1) lookups.
        # We iterate through each number, and if it's the start of a sequence (i.e., n-1 is not in the set),
        # we then check how long the sequence is by counting the consecutive numbers.
        # The time complexity for this solution is approximately O(n), given that each number is processed at most twice.

        if not nums:
            return 0

        streak = 1
        longest_streak = 1
        nums = set(nums)  # Convert list to set for efficient lookups

        for n in nums:
            # Check if the current number is the start of a sequence
            if n - 1 not in nums:
                current_n = n
                # Check how long the sequence is
                while current_n + 1 in nums:
                    streak += 1
                    current_n += 1
                longest_streak = max(longest_streak, streak)
                streak = 1  # Reset streak for the next potential sequence

        return longest_streak
