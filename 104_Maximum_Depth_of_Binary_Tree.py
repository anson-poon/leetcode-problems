# https://leetcode.com/problems/maximum-depth-of-binary-tree/?envType=problem-list-v2&envId=eadewi47

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:        
        def helper(node, cur_depth):
            # Base case: reaching left node or empty tree
            if not node:
                return cur_depth

            # Recurse down the left and right subtrees while incrementing cur_depth by 1
            left_depth = helper(node.left, cur_depth + 1)
            right_depth = helper(node.right, cur_depth + 1)
            
            # The max depth for the current node will be the max of left and right depths
            return max(left_depth, right_depth)
        
        return helper(root, 0)
