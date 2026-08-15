from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n=len(strs)
        Hashmap=defaultdict(list)
        for i in range(n):
            s=strs[i]
            m=len(s)
            occurrences_s=[0]*26
            for j in range(m):
                occurrences_s[ord(s[j])-ord("a")] += 1 
            occ=tuple(occurrences_s)
            Hashmap[occ].append(s)
        return list(Hashmap.values())


