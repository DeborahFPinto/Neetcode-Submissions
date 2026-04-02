# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        result = ListNode(0)
        saveHead = result
        vall1 = 0
        vall2 = 0


        while l2 or l1:
            
            if l1:
                vall1 = l1.val
            else:
                vall1 = 0

            if l2:
                vall2 = l2.val
            else:
                vall2 = 0

            temp = vall1 + vall2 + carry
            carry = temp // 10
            temp = temp % 10
            
            result.next = ListNode(temp)

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            result = result.next

        if carry != 0:
            result.next = ListNode(carry)

        return saveHead.next