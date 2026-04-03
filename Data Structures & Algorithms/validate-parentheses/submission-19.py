class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        maps = {')':'(', '}':'{', ']':'['}
        for char in s:
            if char in['(', '[','{']:
                stack.append(char)
            elif char in maps:
                if stack and stack.pop() == maps[char]:
                    pass
                else:
                    return False
        if not stack:
            return True
        return False
