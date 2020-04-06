# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 23:56:56 2018

@author: Evan_He
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return head
        head1 = head
        #head2 = head
        t = 1
        while head1.next!=None:
            t+=1
            head1 = head1.next
        t1 = 1
        k = k%t
        while t1<=(t-k):
            head1.next = ListNode(head.val)
            head1 = head1.next
            head = head.next
            t1+=1
        
        #while t1<=(t-k):
        return head
        
  