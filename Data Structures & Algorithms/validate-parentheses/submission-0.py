class Solution:
    def isValid(self, s: str) -> bool:
        ### stack --> LIFO so first add {, (, ), 

        matches = {")": "(", 
               "}": "{", 
               "]": "["}

        stack = []

        for i in s: 
            if i in matches:  # Check if it's a closing bracket
                if not stack or stack[-1] != matches[i]:  # Check for matching opening bracket
                    return False  # Mismatched brackets
                stack.pop()  # Pop the last item if it matches

            else:
                stack.append(i)  # Add opening brackets to the stack
            
        return len(stack) == 0  # Return True if all brackets match