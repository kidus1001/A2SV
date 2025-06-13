# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        list1 = []
        list2 = []
        while (l1 != None):
            list1.append(l1.val)
            l1 = l1.next
        while (l2 != None):
            list2.append(l2.val)
            l2 = l2.next
        list1 = list1[::-1]
        list2 = list2[::-1]

        num1 = 0
        num2 = 0

        for i in range(len(list1)):
            num1 = (num1 * 10) + list1[i]

        for i in range(len(list2)):
            num2 = (num2 * 10) + list2[i]

        result = num1+num2

        if result == 0:
            return ListNode(0)
        
        dummy = ListNode(0)
        current = dummy
        while(result != 0):
            rem = result % 10
            current.next = ListNode(rem)
            current = current.next
            result //= 10
        return dummy.next



        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        