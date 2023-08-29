class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minStack) == 0 or self.getMin() > val:
            self.minStack.append(val)
        else:
            self.minStack.append(self.getMin())
    def pop(self) -> None:
        self.stack.pop(-1)
        self.minStack.pop(-1)

    def top(self) -> int:
        if len(self.stack) == 0:
            return []
        return self.stack[len(self.stack)-1]
        
    def getMin(self) -> int:
        if len(self.minStack) == 0:
            return []
        return self.minStack[len(self.minStack)-1]