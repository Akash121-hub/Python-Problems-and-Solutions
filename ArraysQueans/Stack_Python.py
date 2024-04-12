class StackUsingList:
    def __init__(self) -> None:
        self.stack = []

    def push(self,item):
        self.stack.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None
    
    def is_empty(self):
        if len(self.stack) == 0:
            return []
        else:
            return self.stack
        
    def size(self):
        if len(self.stack) > 0:
            return len(self.stack)