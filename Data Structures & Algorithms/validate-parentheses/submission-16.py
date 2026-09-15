class Solution:
    def isValid(self, s: str) -> bool:
        n=len(s)
        corr={"(":")","[":"]","{":"}"}
        stack=[]
        for c in s:
            if c in corr:
                stack.append(c)
            else :
                if not stack:
                    return False
                a=stack[-1]
                if c != corr[a]:
                    return False
                else:
                    stack.pop()
        if not stack:
            return True
        return False
