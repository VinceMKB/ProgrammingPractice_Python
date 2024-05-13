import sys
import math

class Solution(object):
    def numTrees(self, n):
        two_n_fact = math.factorial(2*n)
        n_plus_one_fact = math.factorial(n + 1)
        n_fact = math.factorial(n)

        equation = two_n_fact // (n_plus_one_fact * n_fact)

        return equation

solution = Solution()
num_in = 6

result = solution.numTrees(num_in)
print(result)