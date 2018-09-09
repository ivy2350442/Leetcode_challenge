"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        if not root:
            return []

        last = [root.val]

        for child in root.children:
            last += self.preorder(child)

        return last
