class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=len(s)
        gauche=0
        droit=n-1
        while gauche < droit :
            while (gauche < droit) and not ("a" <= s[gauche]<= "z" or "A" <= s[gauche]<= "Z" or "0" <= s[gauche] <= "9"):
                gauche = gauche + 1
            while (gauche < droit) and not ("a" <= s[droit]<= "z" or "A" <= s[droit]<= "Z" or "0" <= s[droit] <= "9"):
                droit = droit - 1
            if (s[gauche].lower() != s[droit].lower()) :
                return False
            gauche = gauche + 1
            droit = droit - 1
         
        return True