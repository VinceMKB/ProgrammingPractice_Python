import sys

class Solution(object):
    def climbStairs(self, n):
        if n == 0:
            return 1
        if n < 0:
            return 0
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


solution = Solution()
stairs_in = 3
result = solution.climbStairs(stairs_in)
print(result)
