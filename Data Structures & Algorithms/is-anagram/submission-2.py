class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        for letter in s:
            if letter in t and (s.count(letter) == t.count(letter)):
                pass
            else:
                return False
        
        return True