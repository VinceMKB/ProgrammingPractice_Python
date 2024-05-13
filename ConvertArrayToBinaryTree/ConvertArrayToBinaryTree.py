import sys

class TreeNode(object):
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

#Height-Balanced Binary Search Tree
class Solution(object):
    
    def sorted_arrayBST(self, nums):
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])

        root.left = self.sorted_arrayBST(nums[:mid])
        root.right = self.sorted_arrayBST(nums[mid + 1:])

        return root
    
    def preOrder(self, node):
        if not node:
            return
        print(node.val)
        self.preOrder(node.left)
        self.preOrder(node.right)

    
solution = Solution()
nums = [-10, -3, 0, 5, 9]
result = solution.sorted_arrayBST(nums)
solution.preOrder(result)
