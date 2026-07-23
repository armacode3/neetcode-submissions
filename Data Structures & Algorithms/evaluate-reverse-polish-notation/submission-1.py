import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {"+" : operator.add, "-" : operator.sub, "*" : operator.mul, "/" : operator.truediv}

        stack = []

        for token in tokens:
            if token in operations:
                right_operand = stack.pop()
                left_operand = stack.pop()

                result = int(operations[token](left_operand, right_operand))

                stack.append(result)
            else:
                stack.append(int(token))

        return stack[-1]

