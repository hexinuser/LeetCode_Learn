# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 19:39:33 2018

@author: Evan_He
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        head_1 = ListNode(0)
        head_1.next = head
        head = head_1
        while head.next != None:
            if head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next
        return head_1.next
                