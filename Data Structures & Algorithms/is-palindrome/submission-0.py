class Solution:
    def isPalindrome(self, s: str) -> bool:
        revStr = ""
        for c in s:
            if c.isalnum():
                revStr += c.lower()
        print(revStr)
        return revStr == revStr[::-1]
        