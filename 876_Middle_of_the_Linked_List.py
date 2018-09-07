# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        s, f = head, head
        while f.next != None:

            s = s.next
            f = f.next.next
            if f == None:
                return s

        return s
        
