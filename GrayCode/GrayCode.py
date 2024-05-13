import sys

class Solution(object):
    def grayCode(self, n):
        if n == 0:
            return ['']
        first_half = self.grayCode(n - 1)
        second_half = first_half.copy()
        first_half = ['0' + code for code in first_half]
        second_half = ['1' + code for code in reversed(second_half)]
        
        return first_half + second_half

        
solution = Solution()
num_in = 4
result = solution.grayCode(num_in)
print(result)