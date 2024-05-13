import sys

class Solution(object):
    def isPalindrome(self, x) -> bool:
        fwd_int = str(x)
        bwd_int = fwd_int[::-1]
        print("Normal Integer: " + fwd_int)
        print("Reversed Integer: " + bwd_int)
        if fwd_int == bwd_int:
            return True
        else:
            return False
    
solution = Solution()
number = 13631
result = solution.isPalindrome(number)
print(result)