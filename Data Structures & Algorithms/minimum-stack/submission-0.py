class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        # FIX: typo + correct min tracking
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        popped_val = self.stack.pop()
        self.minStack.pop()

        print(f"POP -> {popped_val}")
        print("STACK     :", self.stack)
        print("MIN STACK :", self.minStack)
        print()

    def top(self) -> int:
        print("TOP ->", self.stack[-1])
        return self.stack[-1]

    def getMin(self) -> int:
        print("MIN ->", self.minStack[-1])
        return self.minStack[-1]

