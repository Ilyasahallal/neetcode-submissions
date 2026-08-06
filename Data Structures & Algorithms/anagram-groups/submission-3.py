class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq_s={}
        freq_t={}
        for c in s :
            freq_s[c]= freq_s.get(c,0)+1
        for c in t :
            freq_t[c]= freq_t.get(c,0)+1
        if (freq_t == freq_s) :
            return True
        return False
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group=[]
        for c in strs:
            l=[]
            for a in strs:
                if self.isAnagram(c,a):
                    l.append(a)
            if (l not in group):
                group.append(l)
        return group


        