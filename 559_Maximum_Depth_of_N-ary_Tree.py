"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """

        if not root:
            return 0

        if not root.children:
            return 1

        depth = []
        for child in root.children:

            depth.append(self.maxDepth(child))

        return max(depth) + 1

        
