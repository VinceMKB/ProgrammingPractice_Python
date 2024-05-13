import sys

class Solution(object):
    def mySquareRoot(self, x) -> int:
        if x < 2:
            return x

        start = 1
        end = x // 2  # No need to start `end` at `x` for x > 3

        while start <= end:
            mid = (start + end) // 2  # Use integer division
            mid_squared = mid * mid
            if mid_squared < x:
                start = mid + 1
            elif mid_squared > x:
                end = mid - 1
            else:
                return mid  # Early return for perfect square match

        return end  # After loop, `end` is the integer part of the sqrt

solution = Solution()
number = 25
result = solution.mySquareRoot(number)
print(f"The root of {number} is {result}")

