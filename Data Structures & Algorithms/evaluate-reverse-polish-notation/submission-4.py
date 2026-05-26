class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        operators = "+-*/"

        for tok in tokens:
            if tok not in operators:
                stack.append(int(tok))
            elif tok in operators:
                number1 = stack.pop()
                number2 = stack.pop()

                if tok == "+":
                    stack.append(number1 + number2)
                elif tok == "-":
                    stack.append(number2 - number1)
                elif tok == "*":
                    stack.append(number2*number1)
                else:
                    stack.append(int(number2/number1))

        return stack[-1]

        