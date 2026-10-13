class MinStack:

    def __init__(self):
        self.stack = None
        self.min = None
        

    def push(self, value: int) -> None:
        if self.stack:
            self.stack.append(value)
            if value < self.min:
                self.min = value
        else:
            self.stack = [value]
            self.min = value

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            if self.stack:
                self.min = min(self.stack)

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.min



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()