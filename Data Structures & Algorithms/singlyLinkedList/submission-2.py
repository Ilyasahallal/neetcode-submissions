class Node:
    def __init__(self,val) : 
        self.val= val
        self.next= None
class LinkedList:
    
    def __init__(self):
        self.head = None

    
    def get(self, index: int) -> int:
        current = self.head
        i=0
        while current and i<index :
            i+=1
            current=current.next
        return current.val if current else -1

        

    def insertHead(self, val: int) -> None:
        new_head = Node(val)
        new_head.next = self.head
        self.head = new_head
        
        

    def insertTail(self, val: int) -> None:
        tail=Node(val)
        if not self.head :
            self.head=tail
            return
        current = self.head
        while current.next :
            current = current.next
        current.next=tail
        

    def remove(self, index: int) -> bool:
        if not self.head:
            return False
        
        # Supprimer la tête
        if index == 0:
            self.head = self.head.next
            return True
        i=0
        current= self.head
        while current and i<index-1 :
            current=current.next
            i+=1
        if not current or not current.next:
            return False
        current.next = current.next.next
        return True
        


        

    def getValues(self) -> List[int]:
        values=[]
        current=self.head
        while current :
            values.append(current.val)
            current=current.next
        return values
        
