"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        ans = []
        stack = [root]

        if not root:
            return ans

        while stack:
            last = stack.pop()
            stack += last.children
            ans.append(last.val)

        return ans[::-1]
