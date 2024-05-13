import sys
import array as arr

class Solution(object):
    def merge(self, num_one, m, num_two, n):
        mergelist = []
        for num in num_one[:m]:
            mergelist.append(num)
        for num in num_two[:n]:
            mergelist.append(num)
        
        mergelist.sort()
        return mergelist
        
solution = Solution()
list_one = [1, 3, 5, 0, 0, 0]
size_one = 3
list_two = [2, 4, 6]
size_two = 3
merged = solution.merge(list_one, size_one, list_two, size_two)
print(merged)
