# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 12:23:22 2019

@author: Evan_He
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        head1 = head
        while head1:
            if head1.next:
                val = head1.val
                head1.val = head1.next.val
                head1 = head1.next
                head1.val = val
                head1 = head1.next
            else:
                return head
        return head