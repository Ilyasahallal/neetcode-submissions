class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=len(s)
        left=0
        right=n-1
        while left<right:
            while not ("a"<= s[left] <= "z" or "0" <= s[left] <= "9" or "A" <= s[left] <= "Z") and (left<right):
                left=left+1
            while not ("a" <= s[right] <= "z" or "0" <= s[right] <= "9" or "A" <= s[right] <= "Z") and (left<right):
                right=right-1
            if s[left].lower() != s[right].lower()  :
                return False
            else:
                left=left+1
                right=right-1
        return True
        