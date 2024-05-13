import sys

class Solution(object):
    def isValid(self, str) -> bool:
        stack = []
        opening_brackets = set(['(', '{', '['])
        closing_brackets_map = {')' : '(', '}' : '{', ']': '['}

        for char in str:
            if char in opening_brackets:
                stack.append(char)
            elif char in closing_brackets_map:
                if not stack or closing_brackets_map[char] != stack.pop():
                    return False
        return not stack

solution = Solution()
in_str = "{([])}"
result = solution.isValid(in_str)
print(result)