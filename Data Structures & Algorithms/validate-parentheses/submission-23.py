class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close = {"}": "{", "]":"[", ")":"("}
        for l in s:
            if l in close:
                if stack and stack.pop() == close[l]:
                    continue
                else:
                    return False
            else:
                stack.append(l)
        if stack:
            return False
        else:
            return True
        # for l in s:
        #     if l in ["(","{","["]:
        #         stack.append(l)
        #     elif l == "}":
        #         if len(stack) != 0 and stack.pop() == "{":
        #             continue
        #         else:
        #             return False
        #     elif l == "]":
        #         if len(stack) != 0 and stack.pop() == "[":
        #             continue
        #         else:
        #             return False
        #     elif l == ")":
        #         if len(stack) != 0 and stack.pop() == "(":
        #             continue
        #         else:
        #             return False
        # if len(stack) == 0:
        #     return True
        # return False
            
        