class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # In this solution, we aim to calculate the product of all elements in the array except for the current element.
        # We use two auxiliary arrays 'left' and 'right' to keep track of the product of elements to the left and right of the current element, respectively.
        # The 'left' array is essentially built using a single multiplier variable, which gets updated as we iterate through 'nums'.
        # The final result for each position is obtained by multiplying the corresponding 'left' and 'right' values.
        # Time complexity for this solution is O(n) where n is the number of elements in 'nums'.

        right = [1] * len(nums)

        # Populate 'right' array such that each element contains product of all elements to its right
        for i in range(len(nums) - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        multiplayer = 1

        # Update the 'right' array to store the final result by multiplying with the 'left' product
        for i in range(len(nums)):
            if i == 0:
                multiplayer = 1
            else:
                multiplayer = multiplayer * nums[i - 1]
            right[i] = multiplayer * right[i]

        return right
