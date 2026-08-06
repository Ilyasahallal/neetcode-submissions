class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m= len(t)
        Dn={}
        Dm={}
        if (n != m ) :
            return False
        for c in s:
            if c not in Dn:
                Dn[c]=s.count(c)
        for c in t:
            if c not in Dm:
                Dm[c]=t.count(c)
        if  (Dm==Dn ) :
            return True
        return False

        