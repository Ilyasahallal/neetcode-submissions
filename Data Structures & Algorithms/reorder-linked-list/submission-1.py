# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        while fast and fast.next :
            slow=slow.next
            fast=fast.next.next
        debut=slow.next
        slow.next=None
        current = debut
        prev=None
        while current :
            nxt=current.next
            current.next = prev
            prev = current
            current=nxt
        primary = head
        secondary = prev
        while primary and secondary :
            tmp=primary.next
            tmp2=secondary.next
            primary.next=secondary
            secondary.next = tmp
            primary = tmp
            secondary = tmp2
        return 
        
            
                



        