# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 12:47:51 2018

@author: Evan_He
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        #node即为当前删除节点位置的后续链表
        node.val = node.next.val
        node.next = node.next.next