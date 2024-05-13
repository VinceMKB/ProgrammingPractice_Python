import sys

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def generate_trees(self, n):
        def generate(start, end):
            trees = []
            if start > end:
                trees.append(None)
            else:
                for root_value in range(start, end + 1):
                    left_trees = generate(start, root_value - 1)
                    right_trees = generate(root_value + 1, end)
                    for left_subtree in left_trees:
                        for right_subtree in right_trees:
                            root = TreeNode(root_value, left_subtree, right_subtree)
                            trees.append(root)
            return trees
        return generate(1, n)
    
    def print_tree(self, node, level=0):
        if node is None:
            return
        self.print_tree(node.right, level + 1)
        print(' ' * 4 * level + '->', node.val)
        self.print_tree(node.left, level + 1)

solution = Solution()
trees = solution.generate_trees(4)
for i, tree in enumerate(trees , start = 1):
    print(f"Tree {i}:")
    solution.print_tree(tree)

                        

        