# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        proxNode = None

        while head is not None:
            
            store = head.next
            head.next = proxNode
            proxNode = head 
            head = store

        
        return proxNode

        