class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        char_set = set()  # Correct way to create a set
        length = 0
        r = 0
        l = 0
        
        while r < n:
            if s[r] not in char_set:
                char_set.add(s[r])  # Use add() for sets, not append()
                length = max(length, r - l + 1)
                r += 1
            else:
                char_set.remove(s[l])
                l += 1
        return length