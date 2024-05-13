import sys

class Solution(object):
    def lengthOflastword(self, s):
        lis = s.split(" ")
        size_str = len(lis[-1])
        return size_str

solution = Solution()
in_str = "sky is blue not pink"
result = solution.lengthOflastword(in_str)
print(result)