# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 10:02:35 2018

@author: Evan_He
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        """#利用数组，额外O(n)空间
        if not head:
            return True
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res == res[::-1]
        """
        if not head or not head.next:
            return True
        n, head_1, head_2 = 1, head, head
        while head_1.next:
            head_1 = head_1.next
            n += 1
        # 反转前半截链表， 完结后 head_2的指针在中点处前一个，同时移动头指针和head_2指针比较
        for i in range(1,n//2):
            now = head_2.next  
            head_2.next=now.next 
            now.next = head   
            head = now 
        head_2 = head_2.next
        if n % 2 == 1:
            head_2 = head_2.next
        while head_2:
            if head_2.val != head.val:
                return False
            head_2 = head_2.next
            head = head.next
        return True

            
 
        