"""
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        
        forward = 0
        t =  l1.val + l2.val
        
        if t >= 10:
            t = t % 10
            forward = 1
        
        l = ListNode(t)
        last = l
        
        l1 = l1.next
        l2 = l2.next
        
        
        while l1 is not None or l2 is not None  or forward > 0:
            
            if l1 is None:
                v1 = 0
            else:
                v1 = l1.val
                l1 = l1.next
                
            if l2 is None:
                v2 = 0
            else:
                v2 = l2.val   
                l2 = l2.next
                
            t = forward+v1+v2
            
            if t >= 10:
                t = t % 10
                forward = 1
            else:
                forward = 0
                
            node = ListNode(t)
    
            last.next = node
            last = node
            
            
        return l


