class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n=len(s2)
        m=len(s1)
        l,r=0,(m-1)
        occurences_s1 = {}
        for c in s1 : 
            occurences_s1[c] = occurences_s1.get(c,0) + 1
        while r<n:
            occurences_window = {}
            for c in s2[l:r+1] : 
                occurences_window[c] = occurences_window.get(c,0) + 1
            if occurences_window == occurences_s1 : 
                return True
            l=l+1
            r=r+1
            
            
        return False

         

        