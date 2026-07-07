class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_n = "".join(i.lower() for i in s if i.isalnum())
        if s_n[::-1] == s_n: 
            return True
        else:
           return False

        