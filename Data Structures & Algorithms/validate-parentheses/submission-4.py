class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        brackets = {')' : '(', '}' : '{', ']' : '['}

        for char in s:
            if char in brackets:
                if len(stack) > 0 and brackets[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0
            
