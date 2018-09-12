"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """

        ans = []
        stack = [root]

        if not root:
            return ans


        while stack:
            level = []
            next_level = []

            for node in stack:
                level.append(node.val)

                for child in node.children:
                    if child:
                        next_level.append(child)

            ans.append(level)
            stack = next_level

        return ans
