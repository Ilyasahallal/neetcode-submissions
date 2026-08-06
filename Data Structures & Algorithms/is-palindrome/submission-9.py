class Solution:
    def isPalindrome(self, s: str) -> bool:
        x="".join(char for char in s if char.isalnum()).lower()
        n=len(x)
        j=n-1
        for i in range(n//2):
            if (x[i] != x[j] ):
                return False
            j=j-1
        return True



        
        