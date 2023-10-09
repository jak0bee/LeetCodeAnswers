import collections


class MinStack(object):

    def __init__(self):
        """
        Initialize the data structure.
        """
        # In this solution, we aim to maintain a stack that supports push, pop, top, and retrieving the minimum element in constant time.
        # We use two deques: 'd' to maintain the stack elements and 'min' to keep track of the minimum elements.
        # The 'min' deque is updated such that its first and last elements always contain the current minimum value of the stack.
        # This allows for O(1) time complexity for the getMin() operation.

        self.d = collections.deque()  # Main stack
        self.min = collections.deque()  # Stack for minimum values

    def push(self, val):
        """
        Push an element onto the stack.
        :type val: int
        :rtype: None
        """
        self.d.append(val)
        # Update the 'min' deque based on the new value
        if not self.min or val < self.min[0]:
            self.min.appendleft(val)
        else:
            self.min.append(val)

    def pop(self):
        """
        Pop the top element from the stack.
        :rtype: None
        """
        # Check and update the 'min' deque based on the top element of the stack
        if self.d[-1] == self.min[0] and self.d[-1] != self.min[-1]:
            self.min.popleft()
        else:
            self.min.pop()
        # Pop the top element from the main stack
        self.d.pop()

    def top(self):
        """
        Get the top element of the stack.
        :rtype: int
        """
        return self.d[len(self.d) - 1]

    def getMin(self):
        """
        Retrieve the minimum element in the stack.
        :rtype: int
        """
        # Return the minimum between the first and last elements of the 'min' deque
        return min(self.min[0], self.min[-1])
