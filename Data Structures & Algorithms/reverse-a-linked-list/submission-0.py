# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        proxNode = None

        while head is not None: # Check the node itself, not head.next
            
            store = head.next   # Save the actual next node
            head.next = proxNode # Reverse the pointer
            proxNode = head     # Move proxNode forward
            head = store

        
        return proxNode

        