class Solution:
    def isValid(self, s: str) -> bool:
        Stack=[]
        OpenToClose={"(" : ")" ,"[" : "]" , "{" : "}"}
        for c in s:
            if c in OpenToClose:
                Stack.append(c)
            else:
                if Stack and  OpenToClose[Stack[-1] ]== c :
                    Stack.pop()
                else :
                    return False
        return False if Stack else True



        