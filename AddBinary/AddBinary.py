import sys

class Solution(object):
    def add_Binary(self, a, b):
        sum = bin(int(a, 2) + int(b, 2))
        print(sum)

Solution.add_Binary(Solution, "1101", "100")

