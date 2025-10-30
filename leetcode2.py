"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode()
        current_ptr = head

        l1_ptr = l1
        l2_ptr = l2
        remain = 0
        while (l1_ptr is not None) or (l2_ptr is not None) or remain != 0:
            
            if l1_ptr is not None:
                x = l1_ptr.val
            else:
                x = 0

            if l2_ptr is not None:
                y = l2_ptr.val
            else:
                y = 0
            
            sum = x + y +remain
            remain = 0
            if(sum>=10):
                sum = sum - 10
                remain = 1
            current_ptr.next = ListNode(sum)

            if l1_ptr is not None:
                l1_ptr = l1_ptr.next
            if l2_ptr is not None:
                l2_ptr = l2_ptr.next

            current_ptr = current_ptr.next

        return head.next
