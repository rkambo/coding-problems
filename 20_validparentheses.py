class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) == 0 or len(s) % 2 != 0 :
            return False
        
        for i, c in enumerate(s):
            if c == "{" or c == "[" or c == "(":
                stack.append(c)
            else:
                if(len(stack) == 0):
                    return False
                top = stack.pop()
                if c == '}' and top != '{':
                    return False
                elif c == ')' and top != '(':
                    return False
                elif c == ']' and top != '[':
                    return False                
        return len(stack) == 0