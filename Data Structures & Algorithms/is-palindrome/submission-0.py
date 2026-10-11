class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=''.join(ch.lower() for ch in s if ch.isalnum())
        a=-1
        for i in range(len(s)):
            if(s[i]!=s[a]):
                return False
            a+=-1
        return True