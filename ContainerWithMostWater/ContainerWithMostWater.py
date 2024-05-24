import sys

class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            #Calculate the area
            current_area = min(height[left], height[right]) * (right - left)
            #Update the maximum area found so far
            max_area = max(max_area, current_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area

solution = Solution()
in_array = [1, 8, 6, 2, 5, 4, 8, 3, 7]
result = solution.maxArea(in_array)
print(f"The total area is: {result}")

in_array = [1, 1]
result = solution.maxArea(in_array)
print(f"The total area is: {result}")
