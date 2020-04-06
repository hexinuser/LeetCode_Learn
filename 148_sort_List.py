# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 21:45:04 2018

@author: Evan_He
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res = []
        while head:
            res.append(head.val)
            head = head.next
        res.sort()
        head = ListNode(0)
        res_node = head
        
        for num in res:
            res_node.next = ListNode(num)
            res_node = res_node.next
        return head.next
        