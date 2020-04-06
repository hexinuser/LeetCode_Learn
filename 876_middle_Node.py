# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 14:23:00 2018

@author: Evan_He
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        k = 0
        result = head
        while result!=None:
            k+=1
            result = result.next
            t = 1
        while t<=int(k/2):
            head = head.next
            t+=1
        return head
