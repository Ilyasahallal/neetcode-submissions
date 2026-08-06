class Solution:
    def isValid(self, s: str) -> bool:
        Stack=[]
        ClosetoOpen={")" : "(" , "]" : "[" , "}" : "{"}
        for c in s:
            if c in ClosetoOpen :
                if Stack and Stack[-1] == ClosetoOpen[c] :
                    Stack.pop()
                else:
                    return False
            else :
                Stack.append(c)
        return True if not Stack else False
        


        