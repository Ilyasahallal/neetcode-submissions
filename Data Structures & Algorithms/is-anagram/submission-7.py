class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n=len(s)
        m=len(t)
        if ( n!=m ):
            return False
        ocurrences_s={}
        ocurrences_t={}
        for i in range(n):
            c=0
            element=s[i]
            if element not in ocurrences_s :
                for j in range(n):
                    if s[j] == element :
                        c=c+1
                ocurrences_s[element] = c
        for i in range(n):
            c=0
            element=t[i]
            if element not in ocurrences_t :
                for j in range(n):
                    if t[j] == element :
                        c=c+1
                ocurrences_t[element] = c
        if ocurrences_t == ocurrences_s :
            return True
        return False
        
        