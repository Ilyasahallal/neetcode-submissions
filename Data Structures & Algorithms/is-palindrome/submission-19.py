class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=len(s)
        left=0
        right=n-1
        while left<right:
            if not (s[left].isalnum()):
                left=left+1
            if not (s[right].isalnum()):
                right=right-1
            if (s[left].lower() != s[right].lower() ) and (s[left].isalnum() and s[right].isalnum()):
                return False
            if (s[left].isalnum() and not(s[right].isalnum())):
                left = left-1
            if (s[right].isalnum() and not(s[left].isalnum())):
                right = right+1
            left=left+1
            right=right-1
        return True



        
        