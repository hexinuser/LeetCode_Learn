# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 00:43:36 2018

@author: Evan_He
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        head1 = head
        while head1.next:
            if head1.val == head1.next.val:
                head1.next = head1.next.next
            else:
                head1 = head1.next
        return head