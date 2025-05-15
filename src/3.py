"""https://leetcode.com/problems/longest-substring-without-repeating-characters/"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """s2"""
        s = "abcadcbb"
        store = {
            "a": [0, 3],    #2
            "b": [1, 6, 7], #5, 1
            "c": [2, 5],    #3
            "d": [4]        #0
        }

        return max_len

        """s1"""
        # if s == "":
        #     return 0
        # i1, i2, max_l = 0, 0, 1 
        # store = [s[0]]

        # while True:
        #     i2 += 1
        #     if i2 >= len(s):
        #         break
        #     if s[i2] not in store:
        #         store.append(s[i2])
        #         max_l = max(max_l, len(store))
        #     else: 
        #         i1 += 1
        #         i2 = i1
        #         store = [s[i1]]
            
        # return max_l 