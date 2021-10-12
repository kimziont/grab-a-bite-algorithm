import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^a-zA-Z0-9]', '', s)
        s = s.lower()
        return s == s[::-1]


test = Solution()
assert test.isPalindrome("A man, a plan, a canal: Panama")

