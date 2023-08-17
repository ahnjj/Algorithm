class MinStack:

    def __init__(self):
        self.stack= []
        self.currentMin = 0
        self.previousMin = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.previousMin:
            self.previousMin.append(val)
            self.currentMin = val
        elif self.currentMin >= val:
            self.previousMin.append(val)
            self.currentMin = val

    def pop(self) -> None:
        a = self.stack.pop()
        if a == self.previousMin[-1]:
            self.previousMin.pop()
            if self.previousMin:
                self.currentMin = self.previousMin[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.currentMin


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()