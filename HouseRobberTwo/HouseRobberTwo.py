import sys

class Solution(object):
    def rob(self, nums):
        stolen_num = 0
        for num in nums[1::2]:
            print(f"The money in house is: R {num}K")
            stolen_num += num
        return stolen_num
    
solution = Solution()
in_array = [1,2,3,1]
result = solution.rob(in_array)
print(f"The stolen amount of money is: {result}")