from structures import Node


class Queue:
    def __init__(self, top = None):
        self.top = top

    def getTop(self):
        return self.top
    
    def push(self, value):
        if self.top is None:
            self.top = Node(value)
        else:
            aux = self.top
            while aux is not None:
                return self.getTop
            
    def peek(self):
        if not self.isEmpty:
            return self.getTop.get_value()
        return None;
             
        

    def pull (self):
        adad
    
    def isEmpty(self):
        asd
