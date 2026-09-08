class Node:
    def __init__(self, val:int): 
        self.val = val
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = Node(0)
    
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        return -1
    def insertHead(self, val: int) -> None:
        new = Node(val)
        new.next = self.head.next
        self.head.next = new
        
    def insertTail(self, val: int) -> None:
        curr = self.head
        while curr.next:
            curr = curr.next 
        curr.next = Node(val)
        
    def remove(self, index: int) -> bool:
        curr = self.head
        i=0
        while curr.next:
            if i == index:
                curr.next = curr.next.next
                return True
            curr = curr.next
            i += 1
        return False
    
    def getValues(self) -> List[int]:
        res = []
        curr = self.head.next
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
            
