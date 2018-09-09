# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """

        ans = []
        stack = [root]
        if not root:
            return ans

        while stack:
            level_node = []
            next_level = []

            for node in stack:
                level_node.append(node.val)

                if node.right:
                    next_level.append(node.right)
                if node.left:
                    next_level.append(node.left)

            ans.append(float(sum(level_node))/len(level_node))
            stack = next_level
        return ans
