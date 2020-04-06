# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 14:10:06 2019

@author: Evan_He
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        n = 0
        head1 = head
        while head1:
            n += 1
            head1 = head1.next
        if n < k or k <= 1:
            return head
        t = n//k
        """#法一 利用递归
        return self.reverseK(head,k,t)
        """ 
        #法二 按正常顺序
        res = ListNode(0)
        p = res
        j = 0
        while j < t:
            p_next = head
            index = 0
            for _ in range(k):
                tail = head.next
                p.next, head.next = head, p.next
                head = tail
            p = p_next
            j += 1
        if head:
            p.next = head
        return res.next
        
    def reverseK(self,head, k,m):
            if m == 0:
                return head
            else:
                now = head.next
                head.next = None
                j = 1
                while j<k:
                    temp = now.next  
                    now.next = head  
                    head = now  
                    now = temp    
                    j += 1
                head1 = head
                while head1.next:
                    head1 = head1.next
                head1.next = self.reverseK(temp, k,m-1)
            return head