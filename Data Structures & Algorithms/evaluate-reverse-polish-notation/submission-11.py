class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for val in range(len(tokens)):
            if tokens[val] not in ["+", "-", "*","/"]:
                stack.append(tokens[val])
            else:
                first = int(stack.pop())
                second = int(stack.pop())
                if tokens[val] == "+":
                    stack.append(first + second)
                elif tokens[val] == "-":
                    stack.append(second - first)
                elif tokens[val] == "*":
                    stack.append(first * second)
                elif tokens[val] == "/":
                    stack.append(second / first)
        return int(stack.pop())