import sys
import array as arr
#This is not in O(Log n) time complexity BUT O(n) time complexity
class Solution(object):
    def search_insert(self, nums, target) -> int:
        for i, num in enumerate(nums):
            if num == target:
                return i
            elif num > target:
                nums.insert(i, target)
                print(nums)
                return i
        return len(nums)
                           
solution = Solution()
numbers = arr.array('i', [2, 3, 5, 6])
target_number = 7
result = solution.search_insert(numbers, target_number)
print(result)