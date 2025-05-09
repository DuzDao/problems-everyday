"""
https://leetcode.com/problems/add-two-numbers/
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """s1"""
        head1, head2 = l1, l2 
        if head1.val + head2.val >= 10:
            plus_one=True 
        else:
            plus_one=False
        
        res_head = ListNode((head1.val + head2.val) % 10)
        res_tmp = res_head
        num1_out_of_val, num2_out_of_val = False, False
        
        while True:
            try:
                num1 = head1.next.val 
                head1 = head1.next
            except:
                num1 = 0
                num1_out_of_val = 1

            try:
                num2 = head2.next.val 
                head2 = head2.next
            except:
                num2 = 0
                num2_out_of_val = 1

            next_num = num1 + num2 + plus_one
            if (next_num == 0) and num1_out_of_val and num2_out_of_val:
                break
            res_tmp.next = ListNode(next_num % 10)
            
            if next_num >= 10:
                plus_one=True 
            else:
                plus_one=False
            
            res_tmp = res_tmp.next 
            
        return res_head 


if __name__ == "__main__":
    l1 = [1,6,0,3,3,6,7,2,0,1]
    l2 = [6,3,0,8,9,6,6,9,6,1]

    nodes_1 = [ListNode(l1_value) for l1_value in l1]
    nodes_2 = [ListNode(l2_value) for l2_value in l2]

    for i in range(len(l1) - 1):
        nodes_1[i].next = nodes_1[i+1]
    
    for i in range(len(l2) - 1):
        nodes_2[i].next = nodes_2[i+1]

    result = Solution().addTwoNumbers(nodes_1[0], nodes_2[0])