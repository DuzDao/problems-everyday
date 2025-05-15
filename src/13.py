"""https://leetcode.com/problems/roman-to-integer/"""

class Solution:
    def romanToInt(self, s: str) -> int:
        x = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        sum = 0
        for i in range(len(s)):
            sum += x[s[i]]
            if x[s[i]] > x[s[i-1]] and i > 0:
                sum -= (2 * x[s[i-1]])
        return sum
