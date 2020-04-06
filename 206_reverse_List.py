# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 00:58:13 2018

@author: Evan_He
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #增加节点，尾插
        """
        a0 =   None
        while head != None:
            a = ListNode(head.val)
            a.next = a0
            head = head.next
            a0 = a 
        return a0
        """
        #递归
        """
        # D,E - D-E(node)-D
        # C,D,E - C E(node) D C
        
        if head == None or head.next == None:
            return head
        node = self.reverseList(head.next) #共享head内存，指针在head.next
        head.next.next = head
        head.next = None #相当于复制当前结点之前的所有结点

        return node
        """
        
        """
        使用三个指针指向：当前节点A，下个节点B，以及下下个节点C。
        遍历时，如下首先记录下下个节点C，然后节点B的指针断开并指向A。然后移动进入下一组。
        A -> B -> C ->D -> E
        A <- B 、 C ->D -> E
        """
        #三指针反转链表
        
        if not head or not head.next:
            return head
        now = head.next
        head.next = None
        while now:
            temp = now.next  #C-D-E
            now.next = head  # B-A
            head = now       # head     B-A
            now = temp           
        return head
        
 


