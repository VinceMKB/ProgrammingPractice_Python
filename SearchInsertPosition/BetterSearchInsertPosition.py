import sys
import array as arr
#The time complexity of this is O(log n)
class Solution(object):
    def search_insert(self, nums, target) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        nums.insert(left, target)
        return left

solution = Solution()
numbers = arr.array('i', [1, 2, 5, 6])
target_number = 3
result = solution.search_insert(numbers, target_number)
print(result)