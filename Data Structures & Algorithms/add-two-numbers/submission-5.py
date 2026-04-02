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


        while l2 != None or l1 != None:
            
            if l1 == None:
                vall1 = 0
            else:
                vall1 = l1.val

            if l2 == None:
                vall2 = 0
            else:
                vall2 = l2.val

            temp = vall1 + vall2 + carry
            carry = temp // 10
            temp = temp % 10
            
            result.next = ListNode(temp)

            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next

            result = result.next

        if carry != 0:
            result.next = ListNode(carry)

        return saveHead.next