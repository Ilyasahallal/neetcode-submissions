class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n=len(s)
        m=len(t)
        occurrences_s = {}
        occurrences_t = {}
        if n!=m : 
            return False
        for i in range(n):
            occurrences_s[s[i]] = occurrences_s.get(s[i],0) + 1
            occurrences_t[t[i]] = occurrences_t.get(t[i],0) + 1

        return occurrences_s == occurrences_t