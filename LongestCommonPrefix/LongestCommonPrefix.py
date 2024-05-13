import sys
import array as arr

class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        shortest = min(strs, key=len)
        for i, c in enumerate(shortest):
            if any(x[i]!= c for x in strs):
                return shortest[:i]
        return shortest


solution = Solution()
words = ["flower", "flow", "flight"]

result = solution.longestCommonPrefix(words)
print(result)
