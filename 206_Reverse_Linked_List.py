# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        #linked list 的宣告
        temp = None
        output = None

        while (head != None):
            output = head

            #非常注意這行指令，不可以放在temp = output 之後
            #指標的概念，會導致原本的1直接指向temp
            #head 下一個linked list
            head = head.next

            output.next = temp
            temp = output

        return output
