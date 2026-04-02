# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        saveHead = head
        listStack = []

        while head != None:
            listStack.append(head)
            head = head.next
        
        tam = len(listStack)
        del listStack[tam - n]
        tam -= 1 
        
        if tam == 0:
            return None

        for i in range(tam - 1):
            listStack[i].next = listStack[i + 1]
        
        (listStack[tam - 1]).next = None
        
        

        return listStack[0]