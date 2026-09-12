class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        length_max=0
        seen=set()
        l,r=0,1
        if not s:
            return 0
        if len(s) == 1 :
            return 1
        seen.add(s[l])
        while r<n:
            while s[r] in seen:
                seen.remove(s[l])
                l=l+1
            seen.add(s[r])
            current_length=len(seen)
            length_max=max(length_max,current_length)
            r=r+1
        return length_max
            