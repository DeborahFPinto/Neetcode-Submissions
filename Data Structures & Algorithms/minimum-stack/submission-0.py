class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        tam = len(self.stack)
        return self.stack[tam - 1]

    def getMin(self) -> int:
        minnum = self.stack[0]
        for num in self.stack:
            if num < minnum:
                minnum = num
        
        return minnum
