#Node
class Node(object):
    def __init__(self, content, next=None):
        self.content = content
        self.next = next


#Linked List
class LinkedList(object):
    def __init__(self):
        self.head = None
        self.next = None
    
    #isEmpty?
    def isEmpty(self):
        return self.head is None
    
    #add
    def add(self, data):
        #empty list
        if self.isEmpty():
            self.head = Node(data)
            return
            
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = Node(data)