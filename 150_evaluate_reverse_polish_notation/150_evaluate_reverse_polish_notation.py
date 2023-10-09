class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        # Solution also posted on LeetCode
        # Here I use a simple one stack approach. We know from the wikipedia page that the result is what is left
        # after adding everything from the start to a new list (or here a stack).
        # For th special characters we should do the operation on the last two added numbers.
        # There is also no need to check for validity as that is specified that the RPN is valid.
        # Time and space complexity of this is O(n).
        result = []
        for s in tokens:
            if s == "+":
                result.append(result.pop() + result.pop())
            elif s == "-":
                one = result.pop()
                two = result.pop()
                result.append(two - one)
            elif s == "*":
                result.append(result.pop() * result.pop())
            elif s == "/":
                one = result.pop()
                two = result.pop()
                result.append(int(float(two) / one))
            else:
                result.append(int(s))
        return result.pop()
