class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Step 1: Check length (quick early exit)
        if len(s) != len(t):
            return False
        
        # Step 2: Create two separate hash tables for frequency counts
        freq_s = {}  # Hash table for string s
        freq_t = {}  # Hash table for string t
        
        # Step 3: Count frequencies in string s
        for char in s:
            freq_s[char] = freq_s.get(char, 0) + 1
        
        # Step 4: Count frequencies in string t  
        for char in t:
            freq_t[char] = freq_t.get(char, 0) + 1
        
        # Step 5: Check if frequency of each character is equal
        return freq_s == freq_t  # Python compares dictionaries directly!