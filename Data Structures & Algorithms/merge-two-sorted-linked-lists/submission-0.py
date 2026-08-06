class Solution:
    def mergeTwoLists(self, a, b):
        if not a: return b
        if not b: return a

        # Always make `a` start with the smaller head
        if a.val > b.val:
            a, b = b, a
        
        head = a

        # Traverse until one list ends
        while a and b:
            # advance `a` until we need to insert `b`
            if a.next and a.next.val <= b.val:
                a = a.next
            else:
                # Insert b node into a
                temp = b
                b = b.next
                temp.next = a.next
                a.next = temp
                a = a.next
        
        return head
