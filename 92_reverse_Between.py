# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 00:45:18 2018

@author: Evan_He
"""

class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        k = 1
        result0 = ListNode(0)
        result = result0
        result2 = None
        while head != None:
            if k<m or k>n:
                result.next = ListNode(head.val)
                result = result.next
                k += 1
                
            else:
                head_node = ListNode(head.val)
                head_node.next = result2
                
                result2 = head_node

                if k == n:
                    while result2:
                        result.next = ListNode(result2.val)
                        result2 = result2.next
                        result = result.next

                k+=1
            head=head.next
        return result0.next
                
                
                