# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 14:33:20 2018

@author: Evan_He
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        tmp =ListNode(0)
        result = tmp
        x0 = 0
        while l1!=None or l2!= None:
            if l1 == None:
                t = l2.val+x0
                l2 = l2.next
            elif l2 == None:
                t = l1.val+x0
                l1 = l1.next
            else:
                t=l1.val+l2.val+x0
                l1 = l1.next
                l2 = l2.next

            result.next = ListNode(t%10)
            result = result.next
            x0 = int(t/10)

        if x0==1:
            result.next = ListNode(1)
        return tmp.next
            