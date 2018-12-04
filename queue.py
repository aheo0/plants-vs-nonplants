#Node
class Node(object):
    def __init__(self, content, next=None):
        self.content = content
        self.next = next


#Queue  FIFO
class Queue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.next = None
    
    #isEmpty?
    def isEmpty(self):
        return self.head is None
    
    #add to the beginning
    def enqueue(self, data):
        if self.isEmpty():
            self.tail = Node(data)
        
        newHead = Node(data, self.head)
        self.head = newHead
        
    #remove from the end
    def dequeue(self):
        #one-queue
        if self.head is self.tail:
            self.head = None
            self.tail = None
        
        #more than one-queue
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