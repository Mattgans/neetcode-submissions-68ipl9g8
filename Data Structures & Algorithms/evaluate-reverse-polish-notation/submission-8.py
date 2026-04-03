class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ["+", "-","*", '/']
        for i in tokens:
            if i in operations:
                ret = 0
                right = stack.pop()
                left = stack.pop()
                if i == "+":
                    ret = right + left
                elif i == "-":
                    ret = left - right
                elif i == "*":
                    ret = right * left
                else:
                    ret = left / right
                stack.append(int(ret))
            else:
                stack.append(int(i))
            print(stack)
        return stack.pop()
            
        