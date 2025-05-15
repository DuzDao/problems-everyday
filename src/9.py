"""https://leetcode.com/problems/palindrome-number"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        """s1"""
        if x < 0:
            return False
        
        return str(x) == str(x)[::-1]
    