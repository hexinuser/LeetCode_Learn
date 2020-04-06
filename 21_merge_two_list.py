# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 23:15:35 2018

@author: Evan_He
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        if l1.val<l2.val:
            a = ListNode(l1.val)
            a.next = self.mergeTwoLists(l1.next, l2)
            return a
        else:
            a = ListNode(l2.val)
            a.next = self.mergeTwoLists(l1, l2.next)
            return a