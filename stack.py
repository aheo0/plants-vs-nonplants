#Node
class Node(object):
    def __init__(self, content, next=None):
        self.content = content
        self.next = next


#Stack  LIFO
class Stack(object):
    def __init__(self):
        self.head = None
        self.top = None
        self.next = None
    
    #isEmpty?
    def isEmpty(self):
        return self.head is None
    
    #add to top
    def push(self, data):
        #empty stack
        if self.isEmpty():
            self.head = Node(data)
            self.top = Node(data)
        
        #not empty stack
        else:
            self.top.next = Node(data)
            self.top = self.top.next
        
    #remove from top
    def pop(self):
        #one-stack
        if self.head is self.top:
            self.head = None
            self.top = None
        
        #more than one-stack
        else:
            temp = self.head
            while temp.next.next is not None:
                temp = temp.next
            #temp.next.next is None
            #temp.next is not None
            remove = temp.next
            #temp -> remove -> None
            remove.content = None
            remove = None