class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        closed_to_open = {')' : '(', '}' : '{', ']' : '['}

        for character in s:

            if character in closed_to_open:
                if stack and stack[-1] == closed_to_open[character]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(character)

        # Stack should be empty if each opening bracket had a closing bracket.
        if (stack):
            return False
        else:
            return True