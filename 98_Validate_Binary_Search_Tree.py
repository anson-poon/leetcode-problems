# https://leetcode.com/problems/validate-binary-search-tree/description/?envType=problem-list-v2&envId=eadewi47

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n) for recursive stack
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        INF = sys.maxsize

        def helper(node, lower, upper):
            # Base case: reaching left node or empty tree
            if not node:
                return True

            # If node value within valid bounds, continue traversing with updated upper/lower bound
            if lower < node.val < upper:
                return helper(node.left, lower, node.val) and helper(node.right, node.val, upper)
            # Node value out of bound
            else:
                return False

        return helper(node=root, lower=(-INF), upper=INF)
