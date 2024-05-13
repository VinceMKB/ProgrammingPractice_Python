import sys
import array as arr

class Solution(object):
    def twosum(self, num, target):
        num_dict = {}
        for i, num in enumerate(nums):
            if target - num in num_dict:
                return [ num_dict[target - num], i]
            num_dict[num] = i
        return []


solution = Solution()
nums = arr.array('i', [3,2,4])
target = 6
result = solution.twosum(nums, target)
print(result)