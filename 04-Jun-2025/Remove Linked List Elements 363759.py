# Problem: Remove Linked List Elements - https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        if not head:
            return head
        myList1 = ListNode(-1)
        myList = myList1
        while head:
            if (head.val != val):
                newNode = ListNode(head.val)
                myList.next = newNode
                myList = myList.next
                head = head.next
            else:
                head = head.next
        return myList1.next


        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        