class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in {"+", "-", "*", "/"}:
                # push numbers as ints
                stack.append(int(t))
            else:
                b = stack.pop()
                a = stack.pop()

                if t == "+":
                    stack.append(a + b)
                elif t == "-":
                    stack.append(a - b)
                elif t == "*":
                    stack.append(a * b)
                elif t == "/":
                    # truncate toward 0
                    stack.append(int(a / b))

        # final result is the only thing left on the stack
        return stack.pop()