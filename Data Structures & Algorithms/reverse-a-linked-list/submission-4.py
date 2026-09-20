# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        before = None
        if node == None :
            return None
        while node.next :
            after = node.next
            node.next = before
            before = node
            node = after
        node.next = before

        return node
    