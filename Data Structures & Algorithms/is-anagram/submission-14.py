class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n=len(s)
        m=len(t)
        occurences_s={}
        occurences_t={}
        if n != m : 
            return False
        for i in range(n):
            occurences_s[s[i]] = occurences_s.get(s[i],0) + 1
        for i in range(m):
            occurences_t[t[i]] = occurences_t.get(t[i],0) + 1    
        return occurences_t == occurences_s