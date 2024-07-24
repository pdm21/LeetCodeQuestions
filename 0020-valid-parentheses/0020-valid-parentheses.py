class Solution:
    def isValid(self, s: str) -> bool:
        closing = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        
        for char in s:
            if char in closing:
                if not stack:
                    return False
                val = stack.pop()
                if val != closing[char]:
                    return False
            else:
                stack.append(char)
        return not stack