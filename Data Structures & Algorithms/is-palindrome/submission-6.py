class Solution:
    def isPalindrome(self, s: str) -> bool:
        x="".join(char for char in s if char.isalnum()).lower()
        n=len(x)
        c=""
        for i in range(n-1,-1,-1):
            c+=x[i]
        if (c==x) :
            return True
        return False

        
        