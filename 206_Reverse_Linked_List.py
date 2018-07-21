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
            #若先執行output.next = temp，則head.next 也會等於 temp
            #head 下一個linked list
            head = head.next

            output.next = temp
            temp = output

        return output
            
