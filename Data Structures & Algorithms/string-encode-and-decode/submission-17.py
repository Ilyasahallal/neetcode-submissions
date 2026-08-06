class Solution:
    def __init__(self):
        self.l = []
    def encode(self, strs: List[str]) -> str:
        s=""   
        x=-1
        for c in strs:
            s=s+c
            x=x+len(c)
            (self.l).append(x)
        return s

    def decode(self, s: str) -> List[str]:
        L=[]
        j=0
        for i in range(len(self.l)):
            fin=self.l[i]+1
            c= s[j:fin]
            L.append(c)
            j=fin
        return L


