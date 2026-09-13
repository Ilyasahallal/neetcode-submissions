class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        elements=set(s)
        max_length = 0
        for c in elements :
            m=k
            l,r=0,0
            while r<n:
                if s[r] == c:
                    r = r+1
                else : 
                    if m != 0 : 
                        m=m-1
                        r = r+1
                    else :
                        while s[l] == c:
                            l=l+1
                        l=l+1
                        m=m+1

                        
                max_length = max(max_length,r-l)    
        return max_length            
                


