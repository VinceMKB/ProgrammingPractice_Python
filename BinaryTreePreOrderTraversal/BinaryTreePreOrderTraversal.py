import sys

class TreeNode(object):
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def createTreeNode(self, data):
        return TreeNode(data)
   #PreOrder (data, left, right) 
    def preOrderTraversal(self, m_root):
        if m_root is None:
            return
        print(m_root.val)
        self.preOrderTraversal(m_root.left)
        self.preOrderTraversal(m_root.right)

solution = Solution()
root = solution.createTreeNode(1)
root.right = solution.createTreeNode(2)
root.right.left = solution.createTreeNode(3)

solution.preOrderTraversal(root)
        