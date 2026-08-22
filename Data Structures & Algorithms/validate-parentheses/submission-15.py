class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        brackets = {
            '(':")",
            "[":"]",
            "{":"}"
        }
        for i in s: 
            if i in brackets: 
                stack.append(i) 
                print("Appended opening")
            else:
                if len(stack)==0: 
                    return False 
                open = len(stack)-1
                if  i != brackets[stack[open]]:
                        return False 
                else: 
                    stack.pop()
        return len(stack)==0
        