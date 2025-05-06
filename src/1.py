"""
https://leetcode.com/problems/two-sum/

AI testcase:
Input: [12, 45, 23, 67, 8, 19, 34, 91, 27, 56, 73, 42, 88, 15, 31, 64, 50, 3, 76, 29, 95, 11, 82, 37, 60, 24, 71, 46, 99, 17, 53, 28, 80, 61, 39, 85, 7, 92, 20, 66, 32, 78, 14, 49, 25, 70, 41, 87, 13, 58, 33, 79, 22, 94, 10, 65, 36, 81, 47, 16, 62, 30, 84, 9, 74, 43, 89, 26, 68, 35, 93, 21, 77, 44, 90, 18, 63, 40, 86, 5, 72, 38, 83, 29, 75, 51, 97, 6, 69, 45, 98, 2, 55, 31, 88, 4, 59]

Output: 100
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """s3 O(n)"""
        mem_dict = {}
        for i in range(len(nums)):
            try:
                return [mem_dict[nums[i]], i]
            except:
                mem_dict[target - nums[i]] = i
                continue

        
        """s2 O(2n)"""
        # for i in range(len(nums)):
        #     tmp = target - nums[i]
        #     try:
        #         return [i, nums[i+1:].index(tmp) + i + 1]
        #     except:
        #         continue

        """s1 O(2n)"""
        # for i in range(len(nums)):
        #     tmp = target - nums[i]
        #     for j in range(i + 1, len(nums)):
        #         if nums[j] == tmp:
        #             return [i, j]
        