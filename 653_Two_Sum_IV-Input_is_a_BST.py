# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False

        s = [root]
        set_t = set()

        for node in s:
            if k-node.val in set_t:
                return True
            set_t.add(node.val)
            if node.right:
                s.append(node.right)
            if node.left:
                s.append(node.left)

        return False
