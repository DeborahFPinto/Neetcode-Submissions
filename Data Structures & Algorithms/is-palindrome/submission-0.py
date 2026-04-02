class Solution:
    def isPalindrome(self, s: str) -> bool:

        filtered = ''.join(char.lower() for char in s if char.isalnum())

        if filtered[::-1] == filtered:
            return True
        else:
            return False