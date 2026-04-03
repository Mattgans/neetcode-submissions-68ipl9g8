class Solution:
    def isValid(self, ss: str) -> bool:
        stack = []
        for s in ss:
            if s in ['(','{','[']:
                stack.append(s)
            else:
                if len(stack) == 0 :
                    return False
                if s == ")":
                    if stack.pop() == "(":
                        continue
                    else:
                        return False
                elif s == "}":
                    if stack.pop() == "{":
                        continue
                    else:
                        return False
                elif s == "]":
                    if stack.pop() == "[":
                        continue
                    else:
                        return False
        if len(stack) == 0:
            return True
        else:
            return False
                
        