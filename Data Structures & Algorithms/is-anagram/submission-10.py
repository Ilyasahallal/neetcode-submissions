class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n=len(s)
        m=len(t)
        ocurrences_s={}
        ocurrences_t={}
        if ( n!=m ):
            return False
        for i in range(n):
            ocurrences_s[s[i]]=ocurrences_s.get(s[i],0)+1
        for j in range(m):
            ocurrences_t[t[j]]=ocurrences_t.get(t[j],0)+1
        if ocurrences_s == ocurrences_t :
            return True
        return False
