class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]
        stack = []
        newOperator = 0

        for i in tokens:
            if i in operators:
                operator = i
                b = int(stack.pop())
                a = int(stack.pop())

                if operator == "+":
                    newOperator = a + b
                elif operator == "-":
                    newOperator = a - b
                elif operator == "*":
                    newOperator = a * b
                elif operator == "/":
                    newOperator = int(a / b)

                stack.append(newOperator)
            else:
                stack.append(i)

        return int(stack[-1])