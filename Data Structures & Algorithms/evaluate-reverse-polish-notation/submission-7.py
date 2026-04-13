class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        #iterate through each string
        for c in tokens:
            # add each string to the stack and when we find a operator we pop off the stack
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop() , stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop() , stack.pop()
                stack.append(int(float(b) / a))
            else:
                # cast int to be able to do these operations
                stack.append(int(c))
        
        return stack[0]
            