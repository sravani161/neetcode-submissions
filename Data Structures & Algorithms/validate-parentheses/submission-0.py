class Solution:
    def isValid(self, s: str) -> bool:
        stack_map = {')':'(','}':'{',']':'['}
        stack = []

        for i in s:
            if i in '([{':
                stack.append(i)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if stack_map[i] != top:
                    return False
        return len(stack) == 0
                    