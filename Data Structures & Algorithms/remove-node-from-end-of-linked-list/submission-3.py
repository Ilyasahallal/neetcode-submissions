# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        N=0 
        while curr :
            N=N+1
            curr=curr.next
        if N==n : 
            return head.next
        i = N-n
        curr=head
        while i!= 1:
            curr=curr.next
            i=i-1
        prev = curr
        middle = curr.next
        after = middle.next
        prev.next = after
        middle.next = None
        return head