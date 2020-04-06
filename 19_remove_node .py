# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 22:11:02 2018

@author: Evan_He
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        probe = head
        probe1 = head
        k = 1
        while k<=n:
            probe = probe.next
            k += 1
        if probe == None:
            return head.next #若链表第一遍历到第n个为最后一个，即删除第一个节点
        while probe.next !=None:  #反之第一个从第n个遍历到最后，集对应保留前几个节点
            probe = probe.next  
            probe1 = probe1.next
        
        probe1.next=probe1.next.next
        return head