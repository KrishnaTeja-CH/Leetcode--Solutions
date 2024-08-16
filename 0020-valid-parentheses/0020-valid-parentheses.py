class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) %2 ==1 :
            return False
        
        stack = []
        for char in s:
            if (char == '(' or char == '{' or char == '['):
                stack.append(char)
            else:
                if len(stack) ==0:
                    return False
                c = stack.pop()
                if not ((c=='(' and char == ')') or
                    (c=='[' and char == ']' ) or
                    (c=='{' and char == '}' )):
                        return False
        return len(stack) == 0