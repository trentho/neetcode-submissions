class MyQueue:

    def __init__(self):
        self.stack = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        #move all contents to get front of stack 
        while len(self.stack) > 1:
            self.stack2.append(self.stack.pop())

        #get the only element left in stack 1 (aka the front)
        res = self.stack.pop()

        #move all contents in stack 2 to stack 1 to get it back in order
        while self.stack2:
            self.stack.append(self.stack2.pop())

        return res
        

    def peek(self) -> int:
        #move all contents to get front of stack 
        while len(self.stack) > 1:
            self.stack2.append(self.stack.pop())

        res = self.stack[-1]

        #move all contents in stack 2 to stack 1 to get it back in order
        while self.stack2:
            self.stack.append(self.stack2.pop())   

        return res
        

    def empty(self) -> bool:
        return not self.stack
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()