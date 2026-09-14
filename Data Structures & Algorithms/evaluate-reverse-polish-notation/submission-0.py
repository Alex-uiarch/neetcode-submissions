
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for x in tokens:
            if x != '+' and x != '-' and x != '*' and x != '/':

                stack.append(int(x))
            else:
                a1 = stack.pop()
                a2 = stack.pop()

                if x == '+':
                    stack.append(a1 + a2)

                elif x == '-':
                    stack.append(a2 - a1)

                elif x == '*':
                    stack.append(a1 * a2)

                else:
                    stack.append(int(a2 / a1))


        return stack[0]



