class Solution:
    def isValid(self, s: str) -> bool:
        valid = {'(':')','{':'}','[':']'}
        stack = []
        ans = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            else:
                if len(stack) != 0:
                    ele = stack.pop()
                    if valid[ele] == i:
                        ans.append(True)
                    else:
                        ans.append(False)
                else:
                    ans.append(False)
        if len(stack) != 0 or False in ans:
            return False 
        return True
                    
        