class Solution:
    def isValid(self, s: str) -> bool:

        mapping = {
            ')': '(', 
            ']': '[',
            '}': '{'
            }
        lst = ['(', '[', '{']

        stack = []
        for x in s:
            if x in lst:
                stack.append(x)
            else:

                if len(stack) == 0:
                    return False
                
                if mapping[x] != stack.pop():
                    return False

                
        if len(stack) == 0:
            return True
        else:
            return False
