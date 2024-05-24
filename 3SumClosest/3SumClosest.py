import sys

class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        closest_sum = float('inf')

        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                if current_sum == target:
                    return closest_sum
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
        return closest_sum

solution = Solution()
in_array = [-1, 2, 1, -4]
target = 1
result = solution.threeSumClosest(in_array, target)
print(result)

